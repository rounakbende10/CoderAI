from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_groq import ChatGroq
from agent.prompts import *
from agent.states import *
from langgraph.graph import StateGraph
from langgraph.prebuilt import create_react_agent
from agent.tools import *
from langgraph.graph import END
from langchain.globals import set_debug,set_verbose

_=load_dotenv()
set_debug(True)
set_verbose(True)
llm=ChatGroq(model_name="deepseek-r1-distill-llama-70b")

def planner_agent(state: dict):
    prompt=planner_prompt(state["user_prompt"])
    resp=llm.with_structured_output(Plan).invoke(prompt)
    if resp is None:
        raise ValueError("Planner agent failed to generate a plan")
    
    return {"plan":resp}

def architect_agent(state: dict):
    plan: Plan=state["plan"]
    resp=llm.with_structured_output(TaskPlan).invoke(architect_prompt(plan.model_dump_json()))
    if resp is None:
        raise ValueError("Architect agent failed to generate a plan")
    resp.plan=plan
    return {"task_plan":resp}

def coder_agent(state: dict):
    coder_state: CoderState=state.get("coder_state")
    if coder_state is None:
        coder_state=CoderState(task_plan=state["task_plan"],current_step_idx=0)
    steps=coder_state.task_plan.implementation_steps
    if coder_state.current_step_idx>=len(steps):
        return {"coder_state":coder_state,"status":"DONE"}
    current_task=steps[coder_state.current_step_idx]
    existing_content=read_file.run(current_task.filepath)
    system_prompt=coder_system_prompt()
    user_prompt=(f"Task: {current_task.task_description}\n"
                 f"File: {current_task.filepath}\n"
                 f"Existing content: \n {existing_content}\n"
                 "Use write_file(path,content) to save your changes."
                 )
    coder_tools=[read_file,write_file,list_files,get_current_directory]
    react_agent=create_react_agent(llm,coder_tools)
    result = react_agent.invoke({"messages":[{"role":"system","content":system_prompt},
                                    {"role":"user","content":user_prompt}]})
    coder_state.current_step_idx+=1
    return {"coder_state":coder_state,"status":"IN_PROGRESS"}
    

graph=StateGraph(dict)
graph.add_node("planner",planner_agent)
graph.add_node("architect",architect_agent)
graph.add_node("coder",coder_agent)
graph.add_edge("planner", "architect")
graph.add_edge("architect", "coder")
graph.add_conditional_edges(
    "coder",
    lambda s: "END" if s.get("status")=="DONE" else "coder",
    {"END":END,"coder":"coder"}
)
graph.set_entry_point("planner")
agent=graph.compile()

if __name__ == "__main__":
    result=agent.invoke({"user_prompt":"Build a simple calculator web app in html css and js"},{"recursion_limit":100})
    print("Final State:",result)



