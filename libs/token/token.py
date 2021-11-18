from bd import cur
from sql_fun.users import users_where_token
from flask import abort


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


def token_null(authorization):
    if not authorization:
        abort(403, "Токен не указан")


def user_null(user):
    if not user:
        abort(403, "Токен не валидный")


def token(request):
    authorization = request.headers.get('authorization')
    # Наличие токена
    token_null(authorization)
    params = {
        "token": authorization
    }
    sql = users_where_token(**params)
    cur.execute(sql)
    user = cur.fetchone()
    # Наличие пользователя
    user_null(user)
    user_map = map_get_user_token(user)
    print(user_map)


def validate_admin(request):
    token(request)


def validate_users():
    pass
