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
### Автодокументирование:
```
localhost:8000/swagger/
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
-----------------------------------------------------

# Авторизация пользователя:

POST url: localhost:8000/api/users/login/
body:
{
    "user": {
        "email": "user1@mail.user",
        "password": "vfrtgb55"
    }
}
-----------------------------------------------------

# Получить данные пользователя:

GET url: localhost:8000/api/user/
header: Authorization, Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NywiZXhwIjoxNjQ0MjI2MTMwfQ.UMrx7-qm6BFpHKQgBsSpd3fUIHZoU3UYHN90mkRgphk
-----------------------------------------------------

# Изменить данные пользователя:
PATCH url: localhost:8000/api/user/
body:
{
    "user": {
        "email": "user2@mail.user", 
        "password": "vfrtgb56"
    }
}   
header: Authorization, Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NywiZXhwIjoxNjQ0MjI2MTMwfQ.UMrx7-qm6BFpHKQgBsSpd3fUIHZoU3UYHN90mkRgphk
-----------------------------------------------------

# Выход пользователя из сессии:
GET url: localhost:8000/api/user/logout/
header: Authorization, Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NywiZXhwIjoxNjQ0MjI2MTMwfQ.UMrx7-qm6BFpHKQgBsSpd3fUIHZoU3UYHN90mkRgphk
-----------------------------------------------------

# Сброс пароля, с отправкой уведомления по email:
PATCH url: localhost:8000/api/user/pass_reset/
body:
{
    "user": {
        "email": "user1@mail.user"
    }
}  
-----------------------------------------------------

# Получение списка задач:
GET url: localhost:8000/api/todo/
-----------------------------------------------------

# Получение одной задачи:
GET url: localhost:8000/api/todo/1/
header: Authorization, Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NywiZXhwIjoxNjQ0MjI2MTMwfQ.UMrx7-qm6BFpHKQgBsSpd3fUIHZoU3UYHN90mkRgphk
-----------------------------------------------------

# Создание задачи:
POST url: localhost:8000/api/todo/1/
body:
{
    "headline":"New headline",
    "description":"New description",
    "deadline":"2022-10-30 15:37",
}
-----------------------------------------------------

# Редактирование задачи:
PATCH url: localhost:8000/api/todo/1/
body:
{
    "headline":"Change headline",
    "description":"Change description",
    "deadline":"2022-10-30 15:37",
    "execute":"0"
}
header: Authorization, Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NywiZXhwIjoxNjQ0MjI2MTMwfQ.UMrx7-qm6BFpHKQgBsSpd3fUIHZoU3UYHN90mkRgphk
-----------------------------------------------------

# Удаление задачи:
DELETE url: localhost:8000/api/todo/1/
header: Authorization, Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NywiZXhwIjoxNjQ0MjI2MTMwfQ.UMrx7-qm6BFpHKQgBsSpd3fUIHZoU3UYHN90mkRgphk
-----------------------------------------------------

# Отметить задачу выполненной с отправкой уведомления на почту:
PATCH url: localhost:8000/api/todo/6/execute/
header: Authorization, Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NywiZXhwIjoxNjQ0MjI2MTMwfQ.UMrx7-qm6BFpHKQgBsSpd3fUIHZoU3UYHN90mkRgphk
-----------------------------------------------------

```