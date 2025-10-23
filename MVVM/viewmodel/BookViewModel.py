from model.book_Model import BookModel
from model.book import Book

class BookViewModel:
    def __init__(self, model: BookModel):
        self.model = model

    def add_book(self, title: str, Code: str, genre: str):        
        if not title or not Code:
            return "El título y el autor no pueden estar vacíos."
        valid_genres = ["Sci-Fi", "Terror", "Romance"]
        
        if genre not in valid_genres:
            return f"Género inválido. Elige uno de: {', '.join(valid_genres)}"

        new_book = Book(title, Code, genre)
        self.model.add_book(new_book)
        return f"Libro '{title}' agregado correctamente."

    def list_books(self):  
        books_by_genre = self.model.books_by_genre
        output = ""
        empty = True

        for genre, books in books_by_genre.items():
            output += f"\n {genre}:\n"
            if books:
                empty = False
                for b in books:
                    output += f"- Titulo: {b['title']}\n- Codigo: {b['Code']} \n"
            else:
                output += "  No hay libros en esta categoría.\n"
        if empty:
            return "No hay libros registrados aún."
        return output