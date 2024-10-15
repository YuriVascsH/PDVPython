import mysql.connector

class Database:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="dbpython"
        )
        self.cursor = self.conexao.cursor()

    def consultar_usuario(self, username):
        self.cursor.execute("SELECT username, password FROM usuarios WHERE username = %s", (username,))
        return self.cursor.fetchone()
