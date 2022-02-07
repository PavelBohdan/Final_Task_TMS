import psycopg2

"""Степы для запросов из базы данных"""


def db_users():
    '''
    Функция подключается к базе данных и возвращает список созданных пользователей
    '''
    db = psycopg2.connect(dbname='postgres', user='postgres',
                          password='postgres', host='localhost')
    users = []
    cursor = db.cursor()
    cursor.execute("""SELECT username FROM auth_user""")
    for name in cursor.fetchall():
        users.append(''.join(name))
    return users


def db_get_test_user_id():

    db = psycopg2.connect(dbname='postgres', user='postgres',
                          password='postgres', host='localhost')
    cursor = db.cursor()
    cursor.execute(
        """SELECT id FROM auth_user""")
    for i in cursor.fetchall():
        if i != '1':
            id = str(i)
    return id


if __name__ == '__main__':
    print(db_users())
    print(db_get_test_user_id())
