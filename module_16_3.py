from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1':'Имя: Example, возраст: 18' }

@app.get('/users')
async def get_users() -> dict:
    return users

@app.post('/user/{usernane}/{age}')
async def post_user(message: str) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = message
    return f'User {user_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, message: str) -> str:
    users[user_id] = message
    return f'User {user_id} has been updated'

@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f'User {user_id} has been deleted'

