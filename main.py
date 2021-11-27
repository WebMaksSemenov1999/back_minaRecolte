from flask import Flask
from app import bp


def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    app.register_blueprint(bp, url_prefix='/api')
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
