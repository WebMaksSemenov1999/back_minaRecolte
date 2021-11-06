#!flask/bin/python
from flask import Flask
from users.users_server import get
app = Flask(__name__)


@app.route('/users')
def usersIndex():
    return get()
