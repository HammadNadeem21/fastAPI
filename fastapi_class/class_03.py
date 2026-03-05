# all about request body
from fastapi import FastAPI
from pydantic import BaseModel

class ItemType (BaseModel):
    name:str
    des:str
    price:float
    tax:float | None = None

app = FastAPI()


@app.post('/item')
async def postRequest(item:ItemType):
    return item



@app.put('/item/{item_id}')
def putRequest(item_id: int, item: ItemType):
    return {
        "item_id": item_id, 
        **item.dict()
    }