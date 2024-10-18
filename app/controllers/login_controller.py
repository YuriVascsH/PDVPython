from services.auth_service import AuthService

class LoginController:
    def __init__(self, auth_service=None):
        self.auth_service = auth_service if auth_service else AuthService()
    
    def fazer_login(self, username, password):
        if self.auth_service.verificar_credenciais(username, password):
            return "Login realizado com sucesso"
        else:
            return "Usuário ou senha incorretos"
