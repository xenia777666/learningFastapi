import fastapi
from pydantic import BaseModel
from sqlalchemy.sql.annotation import Annotated

app = fastapi.FastAPI()


class STaskAdd(BaseModel): #pydantic схема
   name: str
   description: str | None = None

tasks=[]

class STask(STaskAdd):
    id: int

@app.post("/tasks") #добавляем таски
async def add_task(
        task: Annotated[STaskAdd, fastapi.Depends()],
):
   tasks.append(task)
   return {"ok": True}

# @app.get("/tasks") #читаем таски
# def get_tasks():
#     task = Task(name="task1")
#     return {"data": task}
gdrdr

