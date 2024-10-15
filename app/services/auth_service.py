from database.database import connectar

class AuthService:
    def __init__(self):
        self.db = connectar()

    def verificar_credenciais(self, username, password):
        user = self.db.consultar_usuario(username)
        if user and user["password"] == password:
            return True
        return False