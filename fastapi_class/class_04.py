# dependency injection
from fastapi import FastAPI, Depends

app = FastAPI()

async def common_parameter(Name:str | None = None, id:int = 1, price:float = 100.00):
    return {
        "Name":Name,
        "Id":id,
        "Price": price
    }


@app.get('/item')
async def getReq(data: dict = Depends(common_parameter)):
    return data