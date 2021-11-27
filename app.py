from flask_restful import Api
from blueprint import bp
from resources.users import Users

api = Api(bp)
api.add_resource(Users, '/users')
