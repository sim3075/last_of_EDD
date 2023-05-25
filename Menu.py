from Desktop import Desktop
class Menu:
    def __init__(self) -> None:
        self.desktop = Desktop()

    def begin(self):
        while True:
            print("======= MENÚ =======")
            print("1. Agregar Carpeta")
            print("2. Agregar Archivo")
            print("3. Modificar Carpeta")
            print("4. Modificar Archivo")
            print("5. Todos los tipos de archivos")
            print("6. Salir")

            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                parent_value_folder = input("Ingrese el nombre de la carpeta en donde se va guardar el nuevo elemento: ")
                new_value_folder = input("Ingrese el nombre de la nueva carpeta: ")
                self.desktop.insert_folder(parent_value_folder, new_value_folder)

            elif opcion == "2":
                parent_value_folder = input("Ingrese el nombre de la carpeta en donde se va guardar el nuevo elemento: ")
                file_name = input("Ingrese el nombre del nuevo archivo: ")
                file_extension = input("Ingrese la extension del nuevo archivo: ")
                file_weight = input("Ingrese el peso del nuevo archivo: ")
                self.desktop.insert_file(parent_value_folder, file_name, file_extension, file_weight)

            elif opcion == "3":
                old_folder = input("Ingrese el nombre de la carpeta a cambiar: ")
                new_folder = input("Ingrese el nuevo nombre: ")
                self.desktop.modify_folder(new_folder, old_folder)

            elif opcion == "4":
                old_file = input("Ingrese el nombre del archivo a cambiar: ")
                new_name = input("Ingrese el nuevo nombre: ")
                new_extension = input("Ingrese la nueva extension: ")
                new_weight = input("Ingresa el nuevo peso: ")
                self.desktop.modify_file(old_file, new_name, new_extension, new_weight)

            elif opcion == "5":
                self.desktop.is_type(self.desktop.root)
                for i in self.desktop.types:
                    print(f"{i} = {self.desktop.types[i]}")
            elif opcion == "6":
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")
            
            self.desktop.imprimir_arbol()

menu = Menu()
menu.begin()
