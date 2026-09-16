import json

def menu():
    print("===========AGRO CONTROL CBA=============")
    print(" ")
    print("1. Gestion de productos")
    print("2. Gestion de lotes productivos")
    print("3. Movimientos de inventario")
    print("4. Registrar venta")
    print("5. Consultar ventas")
    print("6. Alertas de stock")
    print("7. Reportes")
    print("8. Guardar datos")
    print("0. Salir")
    print(" ")

def cargar_productos():
    try:
        with open("agrocontrol_cba/data/productos.json", "r") as archivo:
            productos = json.load(archivo)
            return productos
    except FileNotFoundError:
        return []

def cargar_lotes():
    try:
        with open("agrocontrol_cba/data/lotes.json", "r") as archivo:
            lotes = json.load(archivo)
            return lotes
    except FileNotFoundError:
        return []

def cargar_movimientos():
    try:
        with open("agrocontrol_cba/data/movimientos.json", "r") as archivo:
            movimientos = json.load(archivo)
            return movimientos
    except FileNotFoundError:
        return []

def cargar_ventas():
    try:
        with open("agrocontrol_cba/data/ventas.json", "r") as archivo:
            ventas = json.load(archivo)
            return ventas
    except FileNotFoundError:
        return []

def guardar_productos():
    with open("agrocontrol_cba/data/productos.json", "w") as archivo:
        json.dump (productos, archivo, indent=4)

def guardar_lotes():
    with open("agrocontrol_cba/data/lotes.json", "w") as archivo:
        json.dump (lotes, archivo, indent=4)

def guardar_movimientos():
    with open("agrocontrol_cba/data/movimientos.json", "w") as archivo:
        json.dump (movimientos, archivo, indent=4)

def guardar_ventas():
    with open("agrocontrol_cba/data/ventas.json", "w") as archivo:
        json.dump (ventas, archivo, indent=4)

productos = cargar_productos()
lotes = cargar_lotes()
movimientos = cargar_movimientos()
ventas = cargar_ventas()


def main():
    control = True
    while(control):
        menu()
        try:
            opc = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Ingrese una opcion valida")
            continue
        match(opc):
            case 8:
                guardar_productos()
                guardar_ventas()
                guardar_lotes()
                guardar_movimientos()
                print("Los datos se han guardado con exito")
            case 0:
                print("Ha salido del sistema correctamente")
                break