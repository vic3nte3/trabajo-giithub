
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
    # pasaje_bus_funciones.py

from pasaje_bus_datos import DESTINOS, mostrar_asientos_disponibles


def comprar_pasaje(destino, requiere_pasaporte=False):
    mostrar_asientos_disponibles(destino, DESTINOS)
    if not DESTINOS[destino]["asientos"]:
        print("No hay asientos disponibles.")
        return

    rut = input("Ingrese su RUT: ").strip()
    if rut in DESTINOS[destino]["pasajeros"]:
        print("Ya tiene un pasaje registrado para este destino.")
        return

    nombre = input("Ingrese su nombre completo: ").strip()

    if requiere_pasaporte:
        tiene_pasaporte = input("¿Tiene pasaporte vigente? (s/n): ").lower()
        if tiene_pasaporte != 's':
            print("No puede comprar pasaje sin pasaporte.")
            return
        pasaporte = input("Ingrese su número de pasaporte: ").strip()
    else:
        pasaporte = None

    try:
        asiento = int(input("Ingrese el número de asiento que desea ocupar: "))
    except ValueError:
        print("Número de asiento inválido.")
        return

    if asiento not in DESTINOS[destino]["asientos"]:
        print("El asiento no está disponible.")
        return

    # Registrar pasajero
    DESTINOS[destino]["pasajeros"][rut] = {
        "nombre": nombre,
        "asiento": asiento,
        "pasaporte": pasaporte
    }
    DESTINOS[destino]["asientos"].remove(asiento)
    print("Pasaje comprado exitosamente.")

def ver_asientos_disponibles():
    for destino in DESTINOS:
        mostrar_asientos_disponibles(destino, DESTINOS)

def ver_lista_pasajeros():
    for destino in DESTINOS:
        print(f"\nPasajeros con destino a {destino}:")
        if not DESTINOS[destino]["pasajeros"]:
            print("  No hay pasajeros registrados.")
        else:
            for rut, datos in DESTINOS[destino]["pasajeros"].items():
                info = f"  RUT: {rut}, Nombre: {datos['nombre']}, Asiento: {datos['asiento']}"
                if destino == "Mendoza":
                    info += f", Pasaporte: {datos['pasaporte']}"
                print(info)
                # main.py

from pasaje_bus_datos import mostrar_menu
from pasaje_bus_funciones import comprar_pasaje, ver_asientos_disponibles, ver_lista_pasajeros

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            comprar_pasaje("Viña del Mar")
        elif opcion == "2":
            comprar_pasaje("Valparaíso")
        elif opcion == "3":
            comprar_pasaje("Mendoza", requiere_pasaporte=True)
        elif opcion == "4":
            ver_asientos_disponibles()
        elif opcion == "5":
            ver_lista_pasajeros()
        elif opcion == "6":
            print("Gracias por usar PasajeBus.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if _name_ == "_main_":
    main()
