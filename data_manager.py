#Bruno1
# Lista global
inventario = []

# ---------------------------
# Funcion para cargar datos iniciales
# ---------------------------
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


# ---------------------------
# Funcion para agregar arboles
# ---------------------------
def agregar_arbol(especie, estado, ubicacion):
    arbol = {
        "especie": especie,
        "estado": estado,
        "ubicacion": ubicacion
    }

    inventario.append(arbol)


# ---------------------------
# Programa principal
# ---------------------------
if __name__ == "__main__":
    inicializar_datos()

    agregar_arbol("Pino", "Sano", "Plaza")
    agregar_arbol("Roble", "Seco", "Parque")

    print(inventario)


    
