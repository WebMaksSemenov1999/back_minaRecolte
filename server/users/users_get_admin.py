from libs.order.order_generation import order_generation
from sql_fun.users import users_select_all
from bd import cur
from libs.request_set import request_json_params
from libs.limit_offset import limit_and_offset
from libs.validate.validate import validate
from libs.token.token import validate_admin
from libs.template.validate_template import is_option_type_str, is_option_type_boolean_number, limit_offset, \
    params_order


# валидация параметров для получение users admin
def validate_params_query_all(params):
    schema = {
        "fio": {
           **is_option_type_str
        },
        "nik": {
            **is_option_type_str
        },
        "email": {
               **is_option_type_str
        },
        "is_active": {
            **is_option_type_boolean_number,
        },
        "is_user": {
            **is_option_type_boolean_number,
        },
        "is_admin": {
            **is_option_type_boolean_number,
        },
        "limit": {
            **limit_offset
        },
        "offset": {
            **limit_offset
        },
        "sort_fio": {
            **params_order,
        },
        "sort_nik": {
            **params_order,
        },
        "sort_email": {
            **params_order,
        },
        "sort_is_admin": {
            **params_order,
        },
        "sort_is_user": {
            **params_order,
        },
        "sort_is_active": {
            **params_order,
        }
    }
    validate(params, schema)


# Параметры сортировка для получение users admin
def get_params_query_sort(request, params_sql):
    name_array_column = ['fio', 'nik', 'email', 'is_admin', 'is_user', 'is_active']
    name_array_query = ['sort_fio', 'sort_nik', 'sort_email', 'sort_is_admin', 'sort_is_user', 'sort_is_active']
    order_generation(request, params_sql, 'order', name_array_column, name_array_query)


# Параметры для получение users admin
def get_params_query_all(params_request):
    limit, offset = limit_and_offset(params_request)
    params_sql = {
        'limit': limit,
        'offset': offset,
    }
    get_params_query_sort(params_request, params_sql)
    return params_sql


# map users admin в виде json
def map_get_user(users):
    res = []
    for user in users:
        res.append({
            'id': user[0],
            'fio': user[1],
            'nik': user[2],
            'email': user[3],
            'avatar': user[5],
            'is_active': user[6],
            'is_admin': user[7],
            'is_user': user[8]
        })
    return res


# получение users admin в виде json
def get_users(request):
    validate_admin(request)
    # параметры мап
    params_request = request_json_params(request)
    # параметры валидация
    validate_params_query_all(params_request)
    # параметры
    params = get_params_query_all(params_request)
    # sql запрос запуск
    your_sql = users_select_all(**params)
    cur.execute(your_sql)
    user = cur.fetchall()
    # sql запрос перевод в json
    userMap = map_get_user(user)
    return userMap
