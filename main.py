from data_manager import listar_arboles

while True:
    print("1. Ver árboles")
    print("2. Agregar")
    print("3. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        listar_arboles()

    elif opcion == "3":
        break
