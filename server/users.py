from sql_fun.users import users_select_all
from bd import conn
from libs.request_set import request_set_array, request_sort_set_array
from libs.limit_offset import limit_and_offset
from libs.parsring_order import parsring_order


def get_params_query_filter(request, params_sql):
    name_array = ['fio', 'nik', 'email', 'is_admin', 'is_user', 'is_active']
    request_set_array(request, name_array, params_sql)


def get_params_query_sort(request, params_sql):
    params_sort = {}
    name_array_column = ['fio', 'nik', 'email', 'is_admin', 'is_user', 'is_active']
    name_array_query = ['sort_fio', 'sort_nik', 'sort_email', 'sort_is_admin', 'sort_is_user', 'sort_is_active']
    request_sort_set_array(request, name_array_column, name_array_query, params_sort)
    params_sql['order'] = parsring_order(params_sort)


def users_get_params_query(request):
    limit, offset = limit_and_offset(request)
    params_sql = {
        'limit': limit,
        'offset': offset,
    }
    get_params_query_filter(request, params_sql)
    get_params_query_sort(request, params_sql)

    return params_sql


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


def get_users(request):
    params = users_get_params_query(request)
    your_sql = users_select_all(**params)
    print(your_sql)
    cur = conn.cursor()
    cur.execute(your_sql)
    user = cur.fetchall()
    userMap = map_get_user(user)
    return userMap
