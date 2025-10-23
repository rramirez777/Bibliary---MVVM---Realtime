import json
import os
from model.book import Book

class BookModel:
    def __init__(self, filename="Books.json"):
        self.filename = filename
        self.books_by_genre = self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return {
            "Sci-Fi": [],
            "Terror": [],
            "Romance": []
        }

    def save_books(self):
        with open(self.filename, "w") as f:
            json.dump(self.books_by_genre, f, indent=4)


    def add_book(self, book:Book):
        if book.genre not in self.books_by_genre:
            self.books_by_genre[book.genre] = []

        self.books_by_genre[book.genre].append(book.__dict__)
        self.save_books()
    
    def get_books(self):
        return self.books_by_genre