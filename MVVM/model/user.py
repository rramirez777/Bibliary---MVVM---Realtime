class User:
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email
        
    def __repr__(self):
        return f"User(username='{self.username}', email='{self.email}', password={self.password})"
    
