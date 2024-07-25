from fastapi import FastAPI, Path

app = FastAPI()

@app.get('/')
async def welcome() -> dict:
    return {'message': 'Главная страница'}

@app.get('/user/{user_id}')
async def news(user_id: int = Path(ge=1, le=100,
               description='Enter User ID', example='20')) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}

@app.get('/user/{username}/{age}')
async def user_info(username: str = Path(max_length=5, min_length=20,
                                       description='Enter username',
                                       example='Urban'),
                    age: int = Path(ge=18, le=120,
               description='Enter age', example='33')) -> dict:
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}
