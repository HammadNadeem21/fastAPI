# Path Parameter
from fastapi import FastAPI

app = FastAPI()

@app.get('/user/{user_id}')
def user(user_id:int):
    return {
        "user_id": user_id
    }


@app.get('/{username}/users/{user_id}')
def users(username:str, user_id:int):
    return {
        "username": username,
        "user_id": user_id
    }