#Bruno

inventario = []

def inicializar_datos():
    global inventario

    inventario = [
        {"especie": "Jacarandá", "estado": "Saludable", "ubicacion": "Plaza San Martin"},
        {"especie": "Roble", "estado": "Enfermo", "ubicacion": "Plaza Mitre"},
        {"especie": "Pino", "estado": "Saludable", "ubicacion": "Parque de la Familia"},
        {"especie": "Ceibo", "estado": "Saludable", "ubicacion": "Plaza Bicentenario"},
        {"especie": "Lapacho", "estado": "Enfermo", "ubicacion": "Barrio Norte"},
        {"especie": "Eucalipto", "estado": "Saludable", "ubicacion": "Ruta 3"},
        {"especie": "Sauce", "estado": "Saludable", "ubicacion": "Paseo del Caminante"},
        {"especie": "Álamo", "estado": "Enfermo", "ubicacion": "Biblioteca Sarmiento"},
        {"especie": "Fresno", "estado": "Saludable", "ubicacion": "Escuela PRoA"},
        {"especie": "Palmera", "estado": "Saludable", "ubicacion": "Entrada de la ciudad"}
    ]

#Roman

def agregar_arbol(especie, estado, ubicacion):
    arbol = {
        "especie": especie,
        "estado": estado,
        "ubicacion": ubicacion
    }
    inventario.append(arbol)
    return "Árbol agregado correctamente"

#Thomas
def listar_arboles():
    for arbol in inventario:
        print(f"Especie: {arbol['especie']} | Estado: {arbol['estado']} | Ubicación: {arbol['ubicacion']}")

