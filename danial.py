from fastapi import FastAPI, Request, Response
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(item: Item):
    return {"item": item}

@app.get("/it/")
async def create_item(item: Item):
    return {"item": item}