import json
import datetime

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

def submenu1():
    print("============Gestion Productos==========")
    print(" ")
    print("1. Registrar Producto")
    print("2. Consultar Productos")
    print("3. Actualizar Producto")
    print("4. Gestionar estado de Producto")
    print("0. Salir")
    print(" ")

def cargar_productos():
    try:
        with open("data/productos.json", "r") as archivo:
            productos = json.load(archivo)
            return productos
    except FileNotFoundError:
        return []

def cargar_lotes():
    try:
        with open("data/lotes.json", "r") as archivo:
            lotes = json.load(archivo)
            return lotes
    except FileNotFoundError:
        return []

def cargar_movimientos():
    try:
        with open("data/movimientos.json", "r") as archivo:
            movimientos = json.load(archivo)
            return movimientos
    except FileNotFoundError:
        return []

def cargar_ventas():
    try:
        with open("data/ventas.json", "r") as archivo:
            ventas = json.load(archivo)
            return ventas
    except FileNotFoundError:
        return []

def guardar_productos():
    with open("data/productos.json", "w") as archivo:
        json.dump (productos, archivo, indent=4)

def guardar_lotes():
    with open("data/lotes.json", "w") as archivo:
        json.dump (lotes, archivo, indent=4)

def guardar_movimientos():
    with open("data/movimientos.json", "w") as archivo:
        json.dump (movimientos, archivo, indent=4)

def guardar_ventas():
    with open("data/ventas.json", "w") as archivo:
        json.dump (ventas, archivo, indent=4)

productos = cargar_productos()
lotes = cargar_lotes()
movimientos = cargar_movimientos()
ventas = cargar_ventas()

def registrar_producto():
    codigo = input("Ingrese el codigo del producto: ").strip().upper()

    if codigo=="":
        print("El codigo no puede estar vacio")
    if " " in codigo:
        print("El codigo no puede tener espacios")

    codigo_repetido = False
    for producto in productos:
        if producto['codigo'] == codigo:
            codigo_repetido = True
            break
    
    if codigo_repetido:
        print("El codigo ingresado se encuentra ya asignado a un producto")
        return

    nombre = input("Ingrese el nombre: ").strip()
    categoria = input("Ingrese la categoria: ").strip()

    if nombre == "" or categoria == "":
        print("El nombre y la categoria no pueden quedar vacios") 
        return

    unidad = input("Ingresa la unidad de medida en la que se vende: ").strip().lower()

    precio = int(input("Ingrese el precio del producto: "))
    try:
        if precio <= 0:
            print("El precio debe ser mayor que cero")
            return
    except ValueError:
        print("El precio debe ser un numero entero")
        return

    stock_minimo = int(input("Ingrese el stock minimo para vender: "))

    producto = {
        "codigo":codigo,
        "nombre":nombre,
        "categoria":categoria,
        "unidad":unidad,
        "precio":precio,
        "stock_minimo":stock_minimo,
        "activo":True
    }
    productos.append(producto)
    print(f"Producto {codigo} registrado correctamente")

def consultar_productos():
    if not productos:
        print("No existen productos registrados")

    print(f"| {"Codigo":<10} | {"Nombre":<10} | {"Categoria":<10} | {"Unidad":<10} | ${"Precio":<10} | {"Min_stock":<10} | {"Activo":<10} |")
    print("-" * 77)
    for producto in productos:
        print(f"| {producto['codigo']:<10} | {producto['nombre']:<10} | {producto['categoria']:<10} | {producto['unidad']:<10} |  {producto['precio']:<10} | {producto['stock_minimo']:<10} | {producto['activo']:<10} |")


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
            case 1:
                control1=True
                while (control1):
                    submenu1()
                    try:
                        opc1 = int(input("Seleccione una opcion: "))
                    except ValueError:
                        print("Ingrese una opcion valida")
                        continue
                    match(opc1):
                        case 1:
                            registrar_producto()
                            guardar_productos()
                        case 2:
                            consultar_productos()
                        case 0:
                            break 
            case 2:
                registrar_lote()

                    
            case 0:
                print("Ha salido del sistema correctamente")
                break

main()