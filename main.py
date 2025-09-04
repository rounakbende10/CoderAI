from agent.graph import agent
from langgraph.graph import StateGraph
from dotenv import load_dotenv
import argparse
import sys
import traceback


_=load_dotenv()

def main():
    print("Hello from coderai!")
    parser=argparse.ArgumentParser(description="coderai")
    parser.add_argument("--recursion-limit","-r",type=int,default=100,help="recursion limit")
    args=parser.parse_args()
    try:
        user_prompt=input("Enter your prompt: ")
        result=agent.invoke({"user_prompt":user_prompt},{"recursion_limit":args.recursion_limit})
        print("Final State:",result)
    except Exception as e:
        print("Error:",e)
        traceback.print_exc()
        sys.exit(1)





if __name__ == "__main__":
    main()
