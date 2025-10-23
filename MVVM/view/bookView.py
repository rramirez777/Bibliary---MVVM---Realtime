from viewmodel.BookViewModel import BookViewModel
from model.book_Model import BookModel

class BookView:
    def __init__(self):
        model = BookModel()  
        self.viewmodel = BookViewModel(model) 

    def menu(self):
        while True:
            print("\MENÚ DE LIBROS 📚")
            print("1. Agregar libro")
            print("2. Ver libros")
            print("3. Salir")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.add_book_view()
            elif opcion == "2":
                self.list_books_view()
            elif opcion == "3":
                print("¡Hasta luego! 👋")
                break
            else:
                print("Opción inválida, intenta de nuevo.")

    def add_book_view(self):
        print("\n Agregar un nuevo libro")
        title = input("Título: ")
        Code = input("Codigo: ")
        
        genre = None
        while genre is None:
            genre = print("Lista de Generos (1-3) ")
            print("1. Sci-FI")
            print("2. Terror")
            print("3. Romance ")
            ask = input ("Selecione un genero (1-3)")
            if ask == "1":
                genre = "Sci-Fi"
            if ask == "2":
                genre = "Terror"
            if ask == "3":
                genre = "Romance"
            else:
                print("Genero no valido")
                
        result = self.viewmodel.add_book(title, Code, genre)
        print(result)

    def list_books_view(self):
        print("\n Lista de libros:")
        print(self.viewmodel.list_books())


if __name__ == "__main__":
    view = BookView()
    view.menu()