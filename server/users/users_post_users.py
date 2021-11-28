from libs.request_set import request_json_body
from libs.validate.validate import validate
from libs.template.validate_template import required_params, params_nik, is_option_type_str


def validate_params_query_all(params):
    schema = {
        "fio": {
            "regulations": {
               **required_params,
            }
        },
        "nik": {
            **params_nik,
        },
        "email": {
            "regulations": {
                **required_params,
            }
        },
        "password": {
            "regulations": {
                **required_params,
            }
        },
        "avatar": {
            **is_option_type_str,
        }
    }
    validate(params, schema)


# регистрация users
def post_users(request):
    # параметры мап
    params_request = request_json_body(request)
    # параметры валидация
    validate_params_query_all(params_request)
    return 1
