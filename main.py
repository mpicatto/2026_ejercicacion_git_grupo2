from data_manager import inicializar_datos, obtener_arboles_enfermos

if __name__ == "__main__":
    inicializar_datos()

    while True:
        print("\n--- MENU ---")
        print("1. Ver árboles enfermos")
        print("2. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            enfermos = obtener_arboles_enfermos()

            print("\nÁrboles enfermos:")
            for arbol in enfermos:
                print(arbol)

        elif opcion == "2":
            break