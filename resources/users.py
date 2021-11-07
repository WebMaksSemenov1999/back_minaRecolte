from flask_restful import Resource

from server.users import get_users
from flask import request


class Users(Resource):
    def get(self):
        return get_users(request)
