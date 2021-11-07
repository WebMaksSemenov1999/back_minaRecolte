from flask_restful import Resource

from libs.limit_offset import limitAndOffset
from server.users import get_users, users_get_params_query
from flask import request


class Users(Resource):
    def get(self):
        limit, offset = limitAndOffset(request)
        # paramsMap = users_get_params_query(request)
        params = {
            'limit': limit,
            'offset': offset,
            # **paramsMap,
        }
        return get_users(params)
