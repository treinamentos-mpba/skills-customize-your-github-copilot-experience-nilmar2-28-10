from typing import Dict, Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str
    description: str = ""
    completed: bool = False


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class Task(TaskCreate):
    id: int


tasks: Dict[int, Task] = {
    1: Task(
        id=1,
        title="Explorar o FastAPI",
        description="Consultar a documentação interativa.",
        completed=False,
    )
}
next_task_id = 2


@app.get("/")
def read_root():
    return {"message": "Task API"}
