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
        
        # --- Parte 2: Funcionalidades principales ---

def comprar_pasaje(destino, requiere_pasaporte=False):
    """Permite al usuario comprar un pasaje para un destino."""
    if destino not in DESTINOS:
        print("Destino no válido.")
        return

    mostrar_asientos_disponibles(destino)
    if not DESTINOS[destino]["asientos"]:
        print("Lo sentimos, no hay asientos disponibles para este destino.")
        return

    rut = input("Ingrese su RUT: ").strip()
    if rut in DESTINOS[destino]["pasajeros"]:
        print("Ya tiene un pasaje registrado para este destino.")
        return

    nombre = input("Ingrese su nombre completo: ").strip()

    pasaporte = None
    if requiere_pasaporte:
        tiene_pasaporte = input("¿Tiene pasaporte vigente? (s/n): ").lower().strip()
        if tiene_pasaporte == 's':
            pasaporte = input("Ingrese su número de pasaporte: ").strip()
        else:
            print("Para este destino se requiere pasaporte. No se puede comprar el pasaje sin él.")
            return

    try:
        asiento = int(input("Ingrese el número de asiento que desea ocupar: "))
    except ValueError:
        print("Número de asiento inválido.")
        return

    if asiento not in DESTINOS[destino]["asientos"]:
        print("El asiento no está disponible o no existe.")
        return

    DESTINOS[destino]["pasajeros"][rut] = {
        "nombre": nombre,
        "asiento": asiento,
        "pasaporte": pasaporte
    }
    DESTINOS[destino]["asientos"].remove(asiento)
    print("Asiento comprado con éxito.")
    print(f"Pasaje comprado exitosamente para {destino}.")

def ver_lista_pasajeros():
    """Muestra la lista de pasajeros registrados para cada destino."""
    print("\n--- Lista de pasajeros ---")
    algun_pasajero_registrado = False
    for destino, datos in DESTINOS.items():
        if datos["pasajeros"]:
            algun_pasajero_registrado = True
            print(f"\nDestino: {destino}")
            for rut, info in datos["pasajeros"].items():
                print(f"  RUT: {rut}, Nombre: {info['nombre']}, Asiento: {info['asiento']}", end="")
                if info['pasaporte']:
                    print(f", Pasaporte: {info['pasaporte']}")
                else:
                    print("")
        else:
            print(f"\nDestino: {destino} - No hay pasajeros registrados.")
    if not algun_pasajero_registrado:
        print("No hay pasajeros registrados en ningún destino.")
        
        # --- Parte 3: Función principal ---

def main():
    """Función principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n1.- Ver asientos disponibles para:")
            print("   a) Viña del Mar")
            print("   b) Valparaíso")
            print("   c) Mendoza")
            sub_opcion = input("Seleccione el destino: ").strip().lower()
            if sub_opcion == "a":
                mostrar_asientos_disponibles("Viña del Mar")
            elif sub_opcion == "b":
                mostrar_asientos_disponibles("Valparaíso")
            elif sub_opcion == "c":
                mostrar_asientos_disponibles("Mendoza")
            else:
                print("Opción de destino inválida.")
        elif opcion == "2":
            print("\n2.- Comprar pasaje para:")
            print("   a) Viña del Mar")
            print("   b) Valparaíso")
            print("   c) Mendoza (requiere pasaporte)")
            sub_opcion = input("Seleccione el destino: ").strip().lower()
            if sub_opcion == "a":
                comprar_pasaje("Viña del Mar")
            elif sub_opcion == "b":
                comprar_pasaje("Valparaíso")
            elif sub_opcion == "c":
                comprar_pasaje("Mendoza", requiere_pasaporte=True)
            else:
                print("Opción de destino inválida.")
        elif opcion == "3":
            ver_lista_pasajeros()
        elif opcion == "4":
            print("Gracias por usar PasajeBus.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if _name_ == "_main_":
    main()
