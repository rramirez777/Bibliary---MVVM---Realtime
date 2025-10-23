from view.bookView import BookView
from view.userView import UserView


def main():
    while True:
        print("\n=== SISTEMA MVVM ===")
        print("1. Usuarios")
        print("2. Libros")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            user_view = UserView()
            user_view.menu()
        elif opcion == "2":
            book_view = BookView()
            book_view.menu()
        elif opcion == "3":
            print(" ¡Hasta luego!")
            break
        else:
            print(" Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()