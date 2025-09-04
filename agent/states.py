from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class File(BaseModel):
    path: str = Field(description="the path of the file")
    purpose: str = Field(description="the purpose of the file")


class Plan(BaseModel):
    name: str = Field(description="the name of the project")
    description: str = Field(description="the description of the project")
    techstack: str = Field(description="the techstack of the project")
    features: list[str] = Field(description="the features of the project")
    files: list[File] = Field(description="the files of the project")

class ImplementationTask(BaseModel):
    filepath: str = Field(description="the filepath of the file")
    task_description: str = Field(description="the task description of the file")

class TaskPlan(BaseModel):
    implementation_steps: list[ImplementationTask]= Field(description="the implementation steps of the project")
    model_config = ConfigDict(extra="allow")

class CoderState(BaseModel):
    task_plan: TaskPlan = Field(description="the task plan of the project")
    current_step_idx: int = Field(0,description="the current step index of the project")
    current_file_content: Optional[str] = Field(None,description="the current file content of the project")