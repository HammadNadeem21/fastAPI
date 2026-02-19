from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def main():
    return {
        "name":"Hammad",
        "email":"hammad@gmail.com",
        "age": 23
    }


@app.post('/user')
def userData(name, email, age):
    return {
        "username": name,
        "userEmail": email,
        "userAge": age
    }