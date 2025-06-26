# --- Parte 1: Datos y funciones auxiliares ---

DESTINOS = {
    "Viña del Mar": {"asientos": list(range(1, 11)), "pasajeros": {}},
    "Valparaíso": {"asientos": list(range(1, 11)), "pasajeros": {}},
    "Mendoza": {"asientos": list(range(1, 11)), "pasajeros": {}}
}

def mostrar_menu():
    """Muestra el menú principal de opciones al usuario."""
    print("\n*** SISTEMA DE PASAJEBUS ***")
    print("1.- Ver asientos disponibles")
    print("2.- Comprar pasaje")
    print("3.- Ver pasajeros registrados")
    print("4.- Salir")

def mostrar_asientos_disponibles(destino_elegido):
    """Muestra los asientos disponibles para un destino específico."""
    if destino_elegido in DESTINOS:
        asientos_disponibles = DESTINOS[destino_elegido]["asientos"]
        if asientos_disponibles:
            print(f"Asientos disponibles para {destino_elegido}: {asientos_disponibles}")
        else:
            print(f"No hay asientos disponibles para {destino_elegido}.")
    else:
        print("Destino no válido.")
