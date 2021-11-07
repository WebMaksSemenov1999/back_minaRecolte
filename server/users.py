from sql_fun.users import users_select_all
from bd import conn


def mapGetUser(users):
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


def getUsers():
    your_sql = users_select_all()
    cur = conn.cursor()
    cur.execute(your_sql)
    user = cur.fetchall()
    userMap = mapGetUser(user)
    return userMap
