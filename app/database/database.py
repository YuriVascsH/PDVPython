import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host="localhost", user="root", password="", database="dbpython"):
        try:
            # Conexão com o banco de dados
            self.conexao = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.conexao.cursor()
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.conexao = None

    def consultar_usuario(self, username):
        try:
            if self.conexao:
                query = "SELECT username, password FROM usuarios WHERE username = %s"
                self.cursor.execute(query, (username,))
                return self.cursor.fetchone()
        except Error as e:
            print(f"Erro ao executar a consulta: {e}")
            return None
        finally:
            # Certifique-se de que o cursor é fechado após a consulta
            if self.cursor:
                self.cursor.close()

    def fechar_conexao(self):
        # Método para fechar a conexão
        if self.conexao:
            self.conexao.close()
            print("Conexão com o banco de dados fechada.")
