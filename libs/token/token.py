from bd import cur
from sql_fun.users import users_where_token
from flask import abort
import datetime


def map_get_user_token(user):
    return {
        'id': user[0],
        'fio': user[1],
        'nik': user[2],
        'email': user[3],
        'avatar': user[4],
        'is_active': user[5],
        'is_admin': user[6],
        'is_user': user[7],
        'token': {
            'value': user[8],
            'active': user[9],
            'date': user[10],
        }
    }


def is_token_null(authorization):
    if not authorization:
        abort(403, "Токен не указан")


def is_user_null(user):
    if not user:
        abort(403, "Токен не валидный")


def is_user_active(user):
    if not user['is_active']:
        abort(403, "Пользователь не активен")


def is_token_validate(token):
    now = datetime.datetime.now()
    if not token['active'] and now > token['date']:
        abort(403, "Токен не валидный")


def is_token(request):
    authorization = request.headers.get('authorization')
    # Наличие токена
    is_token_null(authorization)
    params = {
        "token": authorization
    }
    sql = users_where_token(**params)
    cur.execute(sql)
    user = cur.fetchone()
    # Наличие пользователя
    is_user_null(user)
    user_map = map_get_user_token(user)
    print(user_map)
    # Активность пользователя
    is_user_active(user_map)
    # Валидность токена
    is_token_validate(user_map['token'])

    return user_map


def validate_admin(request):
    users = is_token(request)
    if not users['is_admin']:
        abort(403, "доступ запрещен")
    return users


def validate_user(request):
    return is_token(request)
