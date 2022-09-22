from fastapi import FastAPI
from pydantic import BaseModel


# 請求主體類
class Item(BaseModel):
    name: str = "test"
    description: str = None
    price: float = 100
    tax: float = None


app = FastAPI()


@app.post("/items")
async def create_item(item: Item):
    return item
