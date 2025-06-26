
DESTINOS = {
    "Viña del Mar": {"asientos": list(range(1, 11)), "pasajeros": {}},
    "Valparaíso": {"asientos": list(range(1, 11)), "pasajeros": {}},
    "Mendoza": {"asientos": list(range(1, 11)), "pasajeros": {}},
}

def mostrar_menu():
    print("\n***** SISTEMA DE PASAJES PASAJEBUS *****")
    print("1.- Comprar pasaje a Viña del Mar")
    print("2.- Comprar pasaje a Valparaíso")
    print("3.- Comprar pasaje a Mendoza (requiere pasaporte)")
    print("4.- Ver asientos disponibles por destino")
    print("5.- Ver lista de pasajeros")
    print("6.- Salir")

def mostrar_asientos_disponibles(destino, destinos):
    disponibles = destinos[destino]["asientos"]
    print(f"Asientos disponibles para {destino}: {disponibles if disponibles else 'Ninguno'}")
