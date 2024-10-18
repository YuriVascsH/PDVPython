from database.database import connectar

class AuthService:
    def __init__(self, database):
        # Em vez de conectar diretamente, passamos o banco de dados via injeção de dependência
        self.db = database

    def verificar_credenciais(self, username, password):
        user = self.db.consultar_usuario(username)
        if user and user["password"] == password:
            return True
        return False