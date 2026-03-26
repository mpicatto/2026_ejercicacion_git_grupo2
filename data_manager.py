# Bruno Bertoni

inventario = []

def inicializar_datos():
    global inventario

    inventario = [
        {"especie": "Jacarandá", "estado": "Saludable", "ubicacion": "Plaza central"},
        {"especie": "Roble", "estado": "Enfermo", "ubicacion": "Av. San Martín"},
        {"especie": "Pino", "estado": "Saludable", "ubicacion": "Parque industrial"},
        {"especie": "Ceibo", "estado": "Saludable", "ubicacion": "Costanera"},
        {"especie": "Lapacho", "estado": "Enfermo", "ubicacion": "Barrio Norte"},
        {"especie": "Eucalipto", "estado": "Saludable", "ubicacion": "Ruta 3"},
        {"especie": "Sauce", "estado": "Saludable", "ubicacion": "Río local"},
        {"especie": "Álamo", "estado": "Enfermo", "ubicacion": "Parque Sarmiento"},
        {"especie": "Fresno", "estado": "Saludable", "ubicacion": "Escuela primaria"},
        {"especie": "Palmera", "estado": "Saludable", "ubicacion": "Entrada de la ciudad"}
    ]


if __name__ == "__main__":
    inicializar_datos()
    print(inventario)