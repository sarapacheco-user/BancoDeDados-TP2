import pymysql
from pymysql import MySQLError


def get_db_connection():
    try:
        # Your connection configuration
        db_config = {
            'host': 'localhost',
            'user': 'teste15',
            'password': 'senha',
            'database': 'lojaderoupas'
        }

        # Attempt to connect to the database
        connection = pymysql.connect(**db_config)
        return connection

    except MySQLError as e:
        # Handle database connection errors
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None  # You can choose to return None or raise an exception depending on your needs
