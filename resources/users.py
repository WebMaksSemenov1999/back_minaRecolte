from flask_restful import Resource

from server.users.users_post_users import post_users
from server.users.users_get_admin import get_users
from flask import request


class Users(Resource):
    # получить пользователей admin all
    def get(self):
        return get_users(request)

    # регистрация пользователя
    def post(self):
        return post_users(request)
