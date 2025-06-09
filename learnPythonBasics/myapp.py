from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
items = []

app = FastAPI()

class Item(BaseModel):
    text: str = None
    is_done: bool = False

@app.get("/")
def root():
    return {"Hello !":"World!!!!!"}

@app.get("/itemlist")
def list_item():
    return items

@app.post("/items")
def create_item(item : str):
    items.append(item)
    return items

@app.post("/itemsm")
def create_item(item : Item):
    items.append(item)
    return items

@app.get("/items")
def create_item(limit : int = 10):
    return items[0:limit]

@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

@app.get("/itemsm/{item_id}")
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
