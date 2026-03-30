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

     def obtener_arboles_enfermos():
    arboles_enfermos = []

    for arbol in inventario:
        if arbol["estado"] == "Enfermo":
            arboles_enfermos.append(arbol)

    return arboles_enfermos

