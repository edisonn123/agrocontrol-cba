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

def submenuLote():
    print("============Gestion de Lotes==============")
    print(" ")
    print("1. Registrar Lote")
    print("2. Sembrar Lote")
    print("3. Cosechar Lote")
    print("4. Desactivar Lote")
    print("5. Consultar Lotes")
    print("0. Salir")
    print(" ")

def submenuMovimientos():
    print("============Movimientos de Inventario===========")
    print(" ")
    print("1. Registrar entrada manual")
    print("2. Registrar salida manual")
    print("3. Consultar movimientos")
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

    nombre = input("Ingrese el nombre: ").strip().lower()
    categoria = input("Ingrese la categoria: ").strip().lower()

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
        "precio":precio_numero,
        "stock_minimo":stock,
        "activo":True,
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
    if codigo == "":
        print("Ingrese un codigo valido")
        return

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

def consultar_productos_nombre():
    if not productos:
        print("No existen productos registrados")

    nombre = input("Ingrese el nombre o parte de el, del producto: ").strip().lower()
    if nombre == "":
        print("Ingrese un nombre valido")
        return

    encontrados = False
    for producto in productos:
        if nombre in producto['nombre']:
            if not encontrados:
                print(" ")
                print(f"| {"Codigo":<12} | {"Nombre":<12} | {"Categoria":<12} | {"Unidad":<12} |  {"Precio":<12} | {"Min_stock":<12} | {"Activo":<12} |")
                print("-" * 77)
                encontrados = True
            print(f"| {producto['codigo']:<12} | {producto['nombre']:<12} | {producto['categoria']:<12} | {producto['unidad']:<12} | ${producto['precio']:<12} | {producto['stock_minimo']:<12} | {producto['activo']:<12} |")
            print(" ")
    if encontrados == False:
        print("No existen productos con ese nombre")


        

def actualizar_producto():
    codigo = input("Ingrese el codigo del producto que va a actualizar: ").strip()

    encontrado = False
    for producto in productos:
        if producto['codigo'] == codigo:
            encontrado = True
            resultado = producto
            break

    if encontrado == False:
        print(" ")
        print("Producto no encontrado")
        print(" ")
        return
    print("================================================")
    print("Presione ENTER para mantener el campo como esta")
    print("================================================")

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
    if nuevo_stock_minimo != "":
        try:
            stock_numero = int(nuevo_stock_minimo)
            if stock_numero <= 0:
                print("El stock minimo tiene que ser mayor que 0, No se actualizo")
            else:
                resultado["stock_minimo"] = stock_numero
        except ValueError:
            print("Numero invalido, No se actualizo")
    print(" ")
    print("Producto actualizado correctamente")
    print(" ")

def gestionar_estado_producto():
    if not productos:
        print("No existen productos registrados")
        return
    codigo = input("Ingrese el codigo del producto que desea gestionar: ")
    encontrados = False
    for producto in productos:
        if producto["codigo"] == codigo:
            encontrados = True
            print(f"Producto {producto['nombre']} en estado: {producto['activo']}")
            opc = input("Desea cambiar el estado: (si/no): ").strip().lower()
            if (opc == "si") or (opc == "s"):
                if producto['activo'] == True:
                    producto['activo'] = False
                    print(" ")
                    print(f"Estado de {producto['nombre']} cambiado [{producto['activo']}] con exito")
                    print(" ")
                elif producto['activo'] == False:
                    producto['activo'] = True
                    print(" ")
                    print(f"Estado de {producto['nombre']} cambiado a [{producto['activo']}] con exito")
                    print(" ")
            elif (opc == "no") or (opc == "n"):
                print(" ")
                print("Proceso de gestion cancelado con exito")
                print(" ")
                return
            else:
                print("Ingrese una opcion valida")
                return
    if encontrados == False:
        print("No existen productos con ese codigo")

def registrar_lote():
    codigo = input("Ingrese el id del lote: ").strip().upper()
    if codigo=="":
        print("El codigo no puede estar vacio")
        return
    if " " in codigo:
        print("El codigo no puede tener espacios")
        return

    codigo_repetido = False
    for lote in lotes:
        if lote['codigo'] == codigo:
            codigo_repetido = True
            break

    if codigo_repetido == True:
        print("El codigo ingresado se encuentra ya esta registrado")
        return
    if not productos:
        print("No existen productos en el inventario para asignar")
        return
    
    codigo_producto = input("Ingrese el codigo del producto que se asignará al lote: ").strip()
    if codigo_producto == "":
        print("Ingrese un codigo valido")
        return
    encontrado = False
    for producto in productos:
        if codigo_producto == producto['codigo']:
            encontrado = True
            if producto['activo'] == False:
                print("El producto esta inactivo, no se puede asignar")
                return
            for lote in lotes:
                if codigo_producto == lote['codigo_producto']:
                    print("El producto ya esta asignado a un lote")
                    return
    if encontrado == False:
        print("No existe un producto con ese codigo")
        return
    try:    
        area_texto = input("Ingrese el area en m2: ")
        area = float(area_texto)
        if area <=0:
            print("El area debe ser mayor que 0")
            return
    except ValueError:
        print("El area debe ser un numero")
        return
    
    lote = {
        'codigo':codigo,
        'codigo_producto':codigo_producto,
        'fecha_siembra':"",
        'area_m2':area,
        'cantidad_producida':0,
        'estado':""
    }
    lotes.append(lote)
    print("")
    print(f"El producto {codigo_producto} se asigno correctamente al lote {codigo}")
    print("")

def sembrar_lote():
    codigo = input("Ingrese el codigo del lote que desea sembrar: ").strip()

    encontrado = False
    for lote in lotes:
        if lote['codigo'] == codigo:
            encontrado = True
            if lote['estado'] == "EN_PRODUCCION":
                print("El lote ya se encuentra sembrado y en produccion")
                return
            if lote['estado'] == "CANCELADO":
                print("El lote esta desactivado y no se puede sembrar")
                return
            lote['fecha_siembra'] = datetime.datetime.now().strftime("%d-%m-%Y")
            lote['estado'] = "EN_PRODUCCION"
            print("")
            print(f"El lote {lote['codigo']} se sembro correctamente en la fecha {lote['fecha_siembra']}")
            print("")
    if encontrado == False:
        print("No se encontro el lote con ese codigo")

def cosechar_lote():
    codigo = input("Ingrese el codigo del lote que desea cosechar: ").strip()

    encontrado = False
    for lote in lotes:
        if lote['codigo'] == codigo:
            encontrado = True
            if lote['estado'] == "COSECHADO":
                print("El lote ya se encuentra cosechado")
                return
            if lote['estado'] == "CANCELADO":
                print("El lote esta desactivado y no se puede cosechar")
                return
            if lote['estado'] != "EN_PRODUCCION":
                print("El lote debe estar sembrado antes de poder cosecharse")
                return

            try:
                cantidad_producida = int(input("Ingrese la cantidad producida: "))
                if cantidad_producida <= 0:
                    print("La cantidad producida debe ser mayor que 0")
                    return
            except ValueError:
                print("La cantidad producida debe ser un numero entero")
                return

            lote['cantidad_producida'] = cantidad_producida
            lote['estado'] = "COSECHADO"

            movimiento = {
                "id": generar_id_movimiento(),
                "producto_codigo": lote['codigo_producto'],
                "tipo": "ENTRADA",
                "cantidad": cantidad_producida,
                "motivo": f"Cosecha lote {lote['codigo']}",
                "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            movimientos.append(movimiento)
            guardar_movimientos()

            print("")
            print(f"El lote {lote['codigo']} se cosecho correctamente con una cantidad de {lote['cantidad_producida']}")
            print(f"Se genero automaticamente la entrada de inventario {movimiento['id']}")
            print("")
            return

    if encontrado == False:
        print("No se encontro el lote con ese codigo")


def gestionar_estado_lote():
    codigo = input("Ingrese el codigo del lote que desea gestionar: ").strip()

    encontrado = False
    for lote in lotes:
        if lote['codigo'] == codigo:
            encontrado = True
            print(f"Lote {lote['codigo']} en estado: {lote['estado']}")

            if lote['estado'] == "COSECHADO":
                print("Un lote cosechado no puede cambiar de estado")
                return

            if lote['estado'] != "CANCELADO":
                opc = input("Desea cancelar este lote: (si/no): ").strip().lower()
                if (opc == "si") or (opc == "s"):
                    lote['estado'] = "CANCELADO"
                    print(" ")
                    print(f"Lote {lote['codigo']} cancelado correctamente")
                    print(" ")
                elif (opc == "no") or (opc == "n"):
                    print("Proceso cancelado con exito")
                else:
                    print("Ingrese una opcion valida")
                return

            if lote['estado'] == "CANCELADO":
                opc = input("Este lote esta cancelado. Desea reactivarlo: (si/no): ").strip().lower()
                if (opc == "si") or (opc == "s"):
                    lote['estado'] = "EN_PRODUCCION"
                    print(" ")
                    print(f"Lote {lote['codigo']} reactivado y puesto nuevamente en produccion")
                    print(" ")
                elif (opc == "no") or (opc == "n"):
                    print("Proceso cancelado con exito")
                else:
                    print("Ingrese una opcion valida")
                return

    if encontrado == False:
        print("No se encontro el lote con ese codigo")

def consultar_lotes():
    if not lotes:
        print("No existen lotes registrados")
        return

    print(" ")
    print(f"| {'Codigo':<10} | {'Producto':<10} | {'Fecha siembra':<15} | {'Area m2':<10} | {'Cant. producida':<16} | {'Estado':<15} |")
    print("-" * 90)
    for lote in lotes:
        print(f"| {lote['codigo']:<10} | {lote['codigo_producto']:<10} | {lote['fecha_siembra']:<15} | {lote['area_m2']:<10} | {lote['cantidad_producida']:<16} | {lote['estado']:<15} |")
    print(" ")


def calcular_stock(codigo_producto):
    stock = 0
    for movimiento in movimientos:
        if movimiento['producto_codigo'] == codigo_producto:
            if movimiento['tipo'] == "ENTRADA":
                stock = stock + movimiento['cantidad']
            elif movimiento ['tipo'] == "SALIDA":
                stock = stock - movimiento['cantidad']
    return stock

def generar_id_movimiento():
    numero = len(movimientos) + 1
    return f"M{numero:04d}"

def registrar_entrada_manual():
    if not productos:
        print("No existen productos registrados")
        return

    codigo = input("Ingrese el codigo del producto: ").strip().upper()
    encontrado = False
    for producto in productos:
        if producto['codigo'] == codigo:
            encontrado = True
            if producto['activo'] == False:
                print("El producto esta inactivo, no se puede registrar entrada")
                return
    if encontrado == False:
        print("No existe un producto con ese codigo")
        return
    try:
        cantidad = int(input("Ingrese la cantidad de entrada: "))
        if cantidad <=0:
            print("La cantidad debe ser mayor que 0")
            return
    except ValueError:
        print("La cantidad debe ser un numero entero")
        return

    motivo = input("Ingrese el motivo de la entrada: ").strip()
    if motivo == "":
        print("El motivo es obligatorio")
        return

    movimiento = {
        "id": generar_id_movimiento(),
        "producto_codigo": codigo,
        "tipo": "ENTRADA",
        "cantidad":cantidad,
        "motivo":motivo,
        "fecha":datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    movimientos.append(movimiento)
    print(" ")
    print(f"Entrada {movimiento['id']} registrada correctamente. Stock actual: {calcular_stock(codigo)}")

def registrar_salida_manual():
    if not productos:
        print("No existen productos registrados")
        return

    codigo = input("Ingrese el codigo del producto: ").strip().upper()
    encontrado = False
    for producto in productos:
        if producto['codigo'] == codigo:
            encontrado = True
            if producto['activo'] == False:
                print("El producto esta inactivo, no se puede registrar salida")
                return
    if encontrado == False:
        print("No existe un producto con ese codigo")
        return

    try:
        cantidad = int(input("Ingrese la cantidad de salida: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor que 0")
            return
    except ValueError:
        print("La cantidad debe ser un numero entero")
        return

    stock_disponible = calcular_stock(codigo)
    if cantidad > stock_disponible:
        print(f"Stock insuficiente. Stock disponible: {stock_disponible}")
        return

    motivo = input("Ingrese el motivo de la salida: ").strip()
    if motivo == "":
        print("El motivo es obligatorio")
        return

    movimiento = {
        "id": generar_id_movimiento(),
        "producto_codigo":codigo,
        "tipo": "SALIDA",
        "cantidad":cantidad,
        "motivo":motivo,
        "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    movimientos.append(movimiento)
    print(" ")
    print(f"Salida {movimiento['id']} registrada correctamente. Stock actual: {calcular_stock(codigo)}")
    print(" ")

def consultar_movimientos():
    if not movimientos:
        print("No existen movimientos registrados")
        return
    
    print(" ")
    print(f"| {'ID':<8} | {'Codigo':<10} | {'Tipo':<10} | {'Cantidad':<10} | {'Motivo':<25} | {'Fecha':<18} |")
    print("-" * 95)
    for movimiento in movimientos:
        print(f"| {movimiento['id']:<8} | {movimiento['producto_codigo']:<10} | {movimiento['tipo']:<10} | {movimiento['cantidad']:<10} | {movimiento['motivo']:<25} | {movimiento['fecha']:<18} |")
    print(" ")

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
                                    case 4:
                                        consultar_productos_nombre()
                                    case 0:
                                        break
                        case 3:
                            actualizar_producto()
                            guardar_productos()
                        case 4:
                            gestionar_estado_producto()
                            guardar_productos()
                        case 0:
                            break 
            case 2:
                control3 = True
                while (control3):
                    submenuLote()
                    try:
                        opc3 = int(input("Seleccione una opcion: "))
                    except ValueError:
                        print("Ingrese una opcion valida")
                        continue
                    match(opc3):
                        case 1:
                            registrar_lote()
                            guardar_lotes()
                        case 2:
                            sembrar_lote()
                            guardar_lotes()
                        case 3:
                            cosechar_lote()
                            guardar_lotes()
                        case 4:
                            desactivar_lote()
                            guardar_lotes()
                        case 5:
                            consultar_lotes()
                        case 0:
                            break
            case 3:
                control4 = True
                while (control4):
                    submenuMovimientos()
                    try:
                        opc4 = int(input("Seleccione una opcion: "))
                    except ValueError:
                        print("Ingrese una opcion valida")
                        continue
                    match(opc4):
                        case 1:
                            registrar_entrada_manual()
                            guardar_movimientos()
                        case 2:
                            registrar_salida_manual()
                            guardar_movimientos()
                        case 3:
                            consultar_movimientos()
                        case 0:
                            break
                
       
            case 0:
                print("Ha salido del sistema correctamente")
                break

main()