
class Book:
    def __init__(self, title: str, Code: str, genre: str):
        self.title = title
        self.Code = Code
        self.genre = genre

    def __repr__(self):
        return f"Book(Titulo:'{self.title}', Codigo:'{self.Code}', Genero:'{self.genre}')"
