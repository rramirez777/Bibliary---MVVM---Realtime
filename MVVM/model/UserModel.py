import json
import os
from model.user import User

class UserModel:
    def __init__(self, filename="Users.json"):
        self.filename = os.path.join(os.path.dirname(__file__), filename)
        self.users = self.load_users()

    def load_users(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    return [User(**user) for user in data]
            except json.JSONDecodeError:
                print("Error leyendo JSON, archivo vacío o corrupto.")
                return []
        return []
    
    def save_users(self):
        with open(self.filename, "w") as f:
            json.dump([user.__dict__ for user in self.users], f, indent=4)

    def add_user(self, user: User):
        self.users.append(user)
        self.save_users()

    def get_users(self):
        return self.users