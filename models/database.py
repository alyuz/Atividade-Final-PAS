import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    """
    Singleton para conexão com o banco de dados MySQL.
    Aplica padrão GoF Singleton e princípio SOLID (SRP, DIP).
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            try:
                cls._instance = super().__new__(cls)
                cls._instance.connection = mysql.connector.connect(
                    host='localhost',
                    database='sustentabilidade',
                    user='root',
                    password=''
                )
            except Error as e:
                print(f"Erro ao conectar ao banco: {e}")
                cls._instance = None
        return cls._instance

    def get_connection(self):
        return self.connection
