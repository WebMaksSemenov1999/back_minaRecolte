import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    # Подключение к существующей базе данных
    conn = psycopg2.connect(
        dbname="MinaRecolte",
        user="postgres",
        password="postgres",
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
