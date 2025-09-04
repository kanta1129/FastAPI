from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#データモデルの定義
class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool]=None #オプション属性(省略可)
@app.post("/items/")
async def create_item(irem: Item): #リクエストボディとしてItemモデルを受け取る
    return irem

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

