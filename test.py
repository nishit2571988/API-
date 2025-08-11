from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_db={
    1:{"name": "John", "age": 30},
    2:{"name": "Jane", "age": 25},
    3:{"name": "Doe", "age": 22},
    4:{"name": "Alice", "age": 28},
    5:{"name": "Bob", "age": 35},
    6:{"name": "Charlie", "age": 27},
    7:{"name": "Eve", "age": 32},
}

class User(BaseModel):
    name: str
    age: int

@app.put("/user_db/data/v1/update/{user_id}")
def user_update(user_id:int,user:User):
    if user_id in user_db:
        user_db[user_id] = user.dict()
        return {"message": "User updated successfully", "user": user_db[user_id]}
    else:   
        return {"message": "User not found"}

@app.delete("/user_db/data/v1/delete/{user_id}")
def delete_user(user_id:int):
    if user_id in user_db:
        del user_db[user_id]
        return {"message": "User deleted successfully"}
    else:
        return {"message": "User not found"}

@app.get("/user_db/data/v1/get/{user_id}")
def getUserDate():
    return user_db;

@app.get("/addtion")
def add(a:int,b:int):
    return a + b

class SubtractModel(BaseModel):
    a: int
    b: int

@app.post("/subtract")
def subtract(model: SubtractModel):
    return model.a - model.b   


print(add(1, 2))