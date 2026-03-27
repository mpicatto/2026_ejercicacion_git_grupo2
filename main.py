# Nombre: TU NOMBRE

from data_manager import *

def menu():
    while True:
        print("\n1. Ver árboles")
        print("2. Agregar árbol")
        print("3. Salir")

        opcion = input("Elegir opción: ")

        if opcion == "3":
            print("Saliendo...")
            break

if __name__ == "__main__":
    menu()
