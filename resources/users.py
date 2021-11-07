from flask_restful import Resource
from  server.users import getUsers

class Users(Resource):
    def get(self):
        return getUsers()