from fastapi import FastAPI, Path, Query

app = FastAPI()

# Главная страница
@app.get("/")
async def read_root():
    return {"message": "Главная страница"}

# Страница администратора
@app.get("/user/admin")
async def read_admin():
    return {"message": "Вы вошли как администратор"}

# Страница пользователя с параметром в пути с валидацией
@app.get("/user/{user_id}")
async def read_user(
    user_id: int = Path(
        ...,
        title="User ID",
        description="Enter User ID",
        gt=0,  # больше 0
        le=100  # меньше или равно 100
    )
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Страница пользователя с параметрами в адресной строке с валидацией
@app.get("/user/{username}/{age}")
async def read_user_info(
    username: str = Path(
        ...,
        title="Username",
        description="Enter username",
        min_length=5,  # длина больше или равно 5
        max_length=20  # длина меньше или равно 20
    ),
    age: int = Path(
        ...,
        title="Age",
        description="Enter age",
        ge=18,  # больше или равно 18
        le=120  # меньше или равно 120
    )
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}


