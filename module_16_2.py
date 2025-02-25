from fastapi import FastAPI, Path

app = FastAPI()




@app.get('/user/admin')
async def welcome_admin() -> dict:
    return {'message': 'Вы вошли как администратор'}

@app.get('/user/{user_id}')
async def welcome_user(user_id: int = Path(ge=0, le=100, description='Enter User ID', example=1)) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}

@app.get('/user/{username}/{age}')
async def user_info(username: str = Path(min_length=5, max_length=20, description='Enter username'),
                    age: int = Path(ge=18, le=120, description='Enter age')) -> dict:
    return {'Информация о пользователе': f'Имя: {username}, Возраст: {age}.'}


@app.get('/')
async def main_page() -> dict:
    return {'message': 'Главная страница'}