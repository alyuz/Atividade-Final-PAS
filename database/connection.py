import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            try:
                cls._instance = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="bd_projetoti",
                    # auth_plugin='mysql_native_password'
                )
            except Error as e:
                print(f"Erro ao conectar ao banco de dados: {e}")
                cls._instance = None
        return cls._instance

    def get_connection(self):
        return self._instance
