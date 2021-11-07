from sql_fun.users import users_select_all
from bd import conn
from libs.request_set import request_set_array


def users_get_params_query(request):
    params = {}
    name_array = ['fio', 'nik', 'email', 'is_admin', 'is_user', 'is_active']
    request_set_array(request, name_array, params)
    return params


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


def get_users(params):
    your_sql = users_select_all(**params)
    print(your_sql)
    cur = conn.cursor()
    cur.execute(your_sql)
    user = cur.fetchall()
    userMap = map_get_user(user)
    return userMap
