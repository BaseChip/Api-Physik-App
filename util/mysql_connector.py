import mysql.connector
import secrets


class MySqlConnector:
    def connect(database):
        return mysql.connector.connect(
                host=secrets.host,
                user=secrets.user,
                password=secrets.password,
                database=database,
            )