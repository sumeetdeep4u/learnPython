from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str = None
    is_done: bool = False

# Default items
items = [
    Item(text="Buy milk", is_done=False),
    Item(text="Walk the dog", is_done=True),
    Item(text="Read a book", is_done=False)
]

@app.get("/")
def root():
    return {"Learn Python FastAPI Opalina!!"}

@app.get("/item-list")
def list_item():
    return items

@app.post("/add-item")
def create_item(item : Item):
    items.append(item)
    return items

@app.get("/item-list-limit")
def create_item(limit : int = 10):
    return items[0:limit]

@app.get("/view-items/{item_id}")
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

@app.delete("/remove-items/{index}")
def remove_item(index: int):
    if 0 <= index < len(items):
        removed = items.pop(index)
        return {"message": "Item removed", "item": removed}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
