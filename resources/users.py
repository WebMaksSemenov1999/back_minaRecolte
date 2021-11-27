from flask_restful import Resource

from server.users.users_post_users import post_users
from server.users.users_get_admin import get_users
from flask import request
from app import bp


class Users(Resource):
    # получить пользователей admin all
    @bp.route('/', methods=['GET'])
    def get(self):
        return get_users(request)

    # регистрация пользователя
    @bp.route('/', methods=['POST'])
    def post(self):
        return post_users(request)
