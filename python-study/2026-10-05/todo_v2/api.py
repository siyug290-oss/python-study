from fastapi import FastAPI
from models import TodoList
from pydantic import BaseModel

app = FastAPI()
t = TodoList()

class NewTodo(BaseModel):
    content:str

@app.get("/")
def read_root():
    print("<<<有人访问了/")
    return{"message":"你好，这是我的第一个接口"}

@app.get("/todos")
def list_todos():
    print("有人访问了todos")
    t.load()
    return{"todos":t.items}

@app.post("/todos")
def add_todos(new: NewTodo):
    t.load()
    t.add(new.content)
    return{"message":"已添加","todos":t.items}

@app.delete("/todos/{index}")
def delete_todo(index:int):
    t.load()
    if t.remove(index):
        return {"message": "已删除", "todos": t.items}
    else:
        return{"message":"序号不存在，没有删除","todos":t.items}

@app.post("/todos/{index}/done")
def done_todo(index:int):
    t.load()
    if t.done(index):
        return{"message":"已标记","todos": t.items}
    else:
        return{"message":"序号不存在,没有标记","todos":t.items}

@app.post("/todos/{index}/undone")
def undone_todos(index:int):
    t.load()
    if t.undone(index):
        return{"message":"已取消标记","todos": t.items}
    else:
        return{"message":"序号不存在，没有取消标记","todos": t.items}
