inventario = []

def listar_arboles():
    for arbol in inventario:
        print(f"Especie: {arbol['especie']}, Estado: {arbol['estado']}, Ubicación: {arbol['ubicacion']}")