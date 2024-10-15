from services.auth_service import AuthService

class LoginController:
    def __init__(self):
        self.auth_service = AuthService()
    
    def fazer_login(self, username, password):
        if self.auth_service.verficar_credenciais(username, password):
            return "Login realizado com sucesso"
        else:
            return "Usuário ou senha incorretos"
