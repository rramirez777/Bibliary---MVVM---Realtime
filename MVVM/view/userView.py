from viewmodel.UserViewModel import UserViewModel
from model.UserModel import UserModel

class UserView:
    def __init__(self):
        self.viewmodel = UserViewModel()

    def menu(self):
        while True:
            print("\n MENÚ DE USUARIOS ")
            print("1. Registrar usuario")
            print("2. Salir")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.add_user_view()
            elif opcion == "2":
                print("Saliendo...")
                break
            else:
                print("Opción inválida, intenta de nuevo.")

    def add_user_view(self):
        print("\n Registrar nuevo usuario")
        name = input("Nombre: ")
        email = input("Correo: ")
        password = input("Contraseña ")

        result = self.viewmodel.add_user(name, email, password)
        print(result)


if __name__ == "__main__":
    view = UserView()
    view.menu()
