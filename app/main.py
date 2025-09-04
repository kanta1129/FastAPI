from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr, conint
import time

app = FastAPI()

#データモデルの定義
class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool]=None #オプション属性(省略可)
@app.post("/items/")
async def create_item(item: Item): #リクエストボディとしてItemモデルを受け取る
    return item

#演習課題１
class UserCreate(BaseModel):
    username: constr(min_length=3,max_length=15)#文字列長制限
    email: EmailStr#Eメール形式
    password: constr(min_length=8)
    full_name: Optional[str]=None
    disabled: bool=False

class MessageCreate(BaseModel):
    sender_id: conint(ge=0)#０以上の整数
    room_id: conint(ge=0)
    test: constr(min_length=1, max_length=1000)
    timestamp: Optional[float]=time.time()#デフォルトは現在時刻

@app.post("/users/")
async def create_User(user: UserCreate):
    return {"message": "user created succesfully", "user_data":user}

@app.post("/messages/")
async def create_email(email: MessageCreate):
    return {"messsage": "email created successfully", "email_data": email}

@app.get("/")
async def read_root():
    return {"message": "Hello World GET"}

@app.post("/")
async def create_root():
    return {"message": "Hello World POST"}

@app.put("/")
async def update_root():
    return {"message": "Hello World PUT"}

@app.patch("/")
async def partial_update_root():
    return {"message": "Hello World PATCH"}

@app.delete("/")
async def delete_root():
    return {"message": "Hello World DELETE"}

# #パスパラメータを用いたAPI
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

# #クエリパラメータを用いたAPI
# @app.get("/items/")
# async def read_items(q: Optional[str] = None):
#     if q:
#         return {"q": q}
#     return {"items": ["item1", "item2", "item3"]}

#演習課題１(パスパラメータ)
@app.get("/hello/{user_name}")
async def read_user(user_name: str):
    return {"message": f"Hello, {user_name}"}

#演習課題２(クエリパラメータ)
@app.get("/info/")
async def get_items(item: Optional[str]=None):
    available_items = ["apple", "banana","orange"]
    if item:
        return {"requested_item": item}
    return{"available_items" : available_items}

