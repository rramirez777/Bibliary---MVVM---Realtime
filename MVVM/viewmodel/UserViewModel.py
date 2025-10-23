from model.user import User
from model.UserModel import UserModel

class UserViewModel:
    def __init__(self):
        self.model = UserModel()
    
    def add_user(self, username: str, email: str, password: str):
        if not username or not email or not password:
            return "Por favor llene todos los campos."
        user = User(username.strip(), email.strip(), password.strip())
        self.model.add_user(user)
        return f"Usuario '{username}' registrado exitosamente."
    
    
    