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

def submenuBuscar():
    print("============Opcion de Busqueda===========")
    print(" ")
    print("1. Listar todos los productos")
    print("2. Listar productos ACTIVOS")
    print("3. Buscar por codigo")
    print("4. Buscar por parte del nombre")
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
        return
    if " " in codigo:
        print("El codigo no puede tener espacios")
        return

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
    if unidad == "":
        print("La unidad no puede quedar vacia")
        return

    precio = input("Ingrese el precio del producto: ")
    if precio == "":
        print("El precio no puede quedar vacio")
        return
    try:
        precio_numero = int(precio)
        if precio_numero <= 0:
            print("El precio debe ser mayor que cero")
            return
    except ValueError:
        print("El precio debe ser un numero entero")
        return

    stock_minimo = input("Ingrese el stock minimo para vender: ").strip()
    if stock_minimo == "":
        print("El stock no puede quedar vacio")
        return
    try:
        stock = int(stock_minimo)
        if stock <= 0:
            print("El stock minimo debe ser mayor que 0")
            return
    except ValueError:
        print("El stock debe ser un numero entero")
        return

    producto = {
        "codigo":codigo,
        "nombre":nombre,
        "categoria":categoria,
        "unidad":unidad,
        "precio":precio,
        "stock_minimo":stock_minimo,
        "activo":True,
        "stock_actual":0
    }
    productos.append(producto)
    print(f"Producto {codigo} registrado correctamente")

def consultar_productos():
    if not productos:
        print("No existen productos registrados")
    print(" ")
    print(f"| {"Codigo":<12} | {"Nombre":<12} | {"Categoria":<12} | {"Unidad":<12} |  {"Precio":<12} | {"Min_stock":<12} | {"Activo":<12} |")
    print("-" * 77)
    for producto in productos:
        print(f"| {producto['codigo']:<12} | {producto['nombre']:<12} | {producto['categoria']:<12} | {producto['unidad']:<12} | ${producto['precio']:<12} | {producto['stock_minimo']:<12} | {producto['activo']:<12} |")
        print(" ")

def consultar_productos_activos():
    if not productos:
        print("No existen productos registrados")

    encontrados = False
    for producto in productos:
        if producto['activo'] == True:
            if not encontrados:
                print(" ")
                print(f"| {"Codigo":<12} | {"Nombre":<12} | {"Categoria":<12} | {"Unidad":<12} |  {"Precio":<12} | {"Min_stock":<12} | {"Activo":<12} |")
                print("-" * 77)
                encontrados = True

            print(f"| {producto['codigo']:<12} | {producto['nombre']:<12} | {producto['categoria']:<12} | {producto['unidad']:<12} | ${producto['precio']:<12} | {producto['stock_minimo']:<12} | {producto['activo']:<12} |")
            print(" ")
    if encontrados == False:
        print("No hay productos activos")

def consultar_productos_codigo():
    if not productos:
        print("No existen productos registrados")

    codigo = input("Ingrese el codigo del producto a buscar: ").strip()

    encontrados = False
    for producto in productos:
        if producto['codigo'] == codigo:
            if not encontrados:
                print(" ")
                print(f"| {"Codigo":<12} | {"Nombre":<12} | {"Categoria":<12} | {"Unidad":<12} |  {"Precio":<12} | {"Min_stock":<12} | {"Activo":<12} |")
                print("-" * 77)
                encontrados = True
            print(f"| {producto['codigo']:<12} | {producto['nombre']:<12} | {producto['categoria']:<12} | {producto['unidad']:<12} | ${producto['precio']:<12} | {producto['stock_minimo']:<12} | {producto['activo']:<12} |")
            print(" ")
    if encontrados == False:
        print("No existen productos con ese codigo")




        

def actualizar_producto():
    codigo = input("Ingrese el codigo del producto que va a actualizar: ").strip()

    encontrado = False
    for producto in productos:
        if producto['codigo'] == codigo:
            encontrado = True
            resultado = producto
            break

    if encontrado == False:
        print("Producto no encontrado")
        return

    print("Presione enter para mantener el campo como esta")
    nuevo_nombre = input(f"Nombre [{resultado['nombre']}]: ").strip()
    if nuevo_nombre != "":
        resultado["nombre"] = nuevo_nombre

    nueva_categoria = input(f"Categoria [{resultado['categoria']}]: ").strip()
    if nueva_categoria != "":
        resultado["categoria"] = nueva_categoria

    nueva_unidad = input(f"Unidad [{resultado['unidad']}]: ").strip()
    if nueva_unidad != "":
        resultado["unidad"] = nueva_unidad

    nuevo_precio = input(f"Precio [{resultado['precio']}]: ").strip()
    if nuevo_precio != "":
        try:
            precio_numero = int(nuevo_precio)
            if precio_numero <= 0:
                print("El precio debe ser mayor que 0, no se actualizo")
            else:
                resultado["precio"] = precio_numero
        except ValueError:
            print("Precio Invalido, No se actualizo")

    nuevo_stock_minimo = input(f"Stock_minimo [{resultado['stock_minimo']}]: ").strip()
    if nuevo_stock_minimo != " ":
        try:
            stock_numero = int(nuevo_stock_minimo)
            if stock_numero <= 0:
                print("El stock minimo tiene que ser mayor que 0, No se actualizo")
            else:
                resultado["stock_minimo"] = stock_numero
        except ValueError:
            print("Numero invalido, No se actualizo")

    print("Producto actualizado correctamente")



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
                            control2 = True
                            while (control2):
                                submenuBuscar()
                                try:
                                    opc2 = int(input("Seleccione una opcion: "))
                                except ValueError:
                                    print("Ingrese una opcion valida")
                                    continue
                                match(opc2):
                                    case 1:
                                        consultar_productos()
                                    case 2:
                                        consultar_productos_activos()
                                    case 3:
                                        consultar_productos_codigo()
                                    case 0:
                                        break
                        case 3:
                            actualizar_producto()
                            guardar_productos()
                        case 0:
                            break 
            case 2:
                registrar_lote()
       
            case 0:
                print("Ha salido del sistema correctamente")
                break

main()