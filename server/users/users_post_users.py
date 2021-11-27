from libs.request_set import request_json
from libs.validate.validate import validate
from libs.template.validate_template import required_params


def validate_params_query_all(params):
    schema = {
        "fio": {
            "regulations": {
               **required_params,
            }
        },
        "nik": {

        },
        "email": {

        },
        "password": {

        },
        "avatar": {

        }
    }
    validate(params, schema)


# регистрация users
def post_users(request):
    # параметры мап
    params_request = request_json(request)
    # параметры валидация
