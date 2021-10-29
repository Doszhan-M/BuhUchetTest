# BuhUchetTest

### Настройка почтового сервера!
```
1. Создать файл secret.env в папке secret

2. Заполнить файл по шаблону:

EMAIL_HOST = smtp сервер почты
EMAIL_HOST_USER = почтовый адрес для отправки писем
EMAIL_HOST_PASSWORD = пароль от почты
EMAIL_PORT = порт почтового сервера
EMAIL_USE_TLS = False или True

SECRET_KEY=секрет кей для джанго

3. Сохранить файл

```

### Примеры запросов для Postman
```
# Регистрация пользователя:
POST url: localhost:8000/api/users/signup/
body:
{
    "user": {
        "username": "user1",
        "email": "user1@mail.user",
        "password": "vfrtgb55"
    }
}

# Авторизация пользователя:
POST url: localhost:8000/api/users/login/
body:
{
    "user": {
        "email": "user1@mail.user",
        "password": "vfrtgb55"
    }
}

# Получить пользователя:
GET url: localhost:8000/api/user/
header: Authorization, Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NiwiZXhwIjoxNjM1NTkxNzY1fQ.-P0Uty9GtmobLZcBD5YJRP2uREQX1N3xvHzAAD6tNcM

# Изменить пользователя:
PATCH url: localhost:8000/api/user/
body:
{
    "user": {
        "email": "user2@mail.user", 
        "password": "vfrtgb56"
    }
}   
header: Authorization, Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NiwiZXhwIjoxNjM1NTkxNzY1fQ.-P0Uty9GtmobLZcBD5YJRP2uREQX1N3xvHzAAD6tNcM

# Выход пользователя из сессии:
GET url: localhost:8000/api/user/logout/
header: Authorization, Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NiwiZXhwIjoxNjM1NTkxNzY1fQ.-P0Uty9GtmobLZcBD5YJRP2uREQX1N3xvHzAAD6tNcM

# Сброс пароля, с отправкой уведомления по email.:
PATCH url: localhost:8000/api/user/pass_reset/
body:
{
    "user": {
        "email": "user1@mail.user"
    }
}   
```