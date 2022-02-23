"""Степы для запросов из базы данных"""


class DataBase:
    def __init__(self, db_connections):
        self.db_connections = db_connections

    def db_users(self):
        '''
        Функция подключается к базе данных и возвращает список созданных пользователей
        '''
        cursor = self.db_connections.cursor()
        cursor.execute("""SELECT username FROM auth_user""")
        users = []
        for name in cursor.fetchall():
            users.append(''.join(name))
        return users
