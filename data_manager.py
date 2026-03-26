inventario = []
def agregar_arbol(especie, estado, ubicacion):
    arbol = {
        "especie": especie,
        "estado": estado,
        "ubicacion": ubicacion
    }

    inventario.append(arbol)

    agregar_arbol("Pino", "Sano", "Plaza")
    agregar_arbol("Roble", "Seco", "Parque")

     print(inventario)  