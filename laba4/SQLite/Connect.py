import sqlite3


class ConnectDB:
    # Функция подключения(создания) к базе данных
    def connDB(self, path_file):
        connection = sqlite3.connect(path_file)
        cursor = connection.cursor()
        return connection, cursor

    # Функция закрытия соединения с БД
    def close_db(self, conn):
        conn.close()
