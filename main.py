import json
import datetime
import csv
import shutil
import os

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
    print("8. Registrar devolucion de venta")
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
    print("4. Gestionar estado de Lote")
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

def submenuVentas():
    print("===========Registrar Venta===========")
    print(" ")
    print("Agregue productos a la venta. Escriba 'FIN' en el codigo para terminar")
    print(" ")

def submenuReportes():
    print("===========Reportes=============")
    print(" ")
    print("1. Reporte de inventario")
    print("2. Reporte de ventas")
    print("3. Reporte de ranking mas vendidos")
    print("4. Reporte de utilidad")
    print("5. Exportar inventario a CSV")
    print("0. Salir")
    print(" ")

def hacer_backup(nombre_archivo):
    try:
        if os.path.exists(nombre_archivo):
            shutil.copy(nombre_archivo, nombre_archivo.replace(".json", "_backup.json"))
    except Exception as error:
        print(f"No se pudo generar la copia de seguridad de {nombre_archivo}: {error}")

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
    hacer_backup("data/productos.json")
    with open("data/productos.json", "w") as archivo:
        json.dump (productos, archivo, indent=4)

def guardar_lotes():
    hacer_backup("data/lotes.json")
    with open("data/lotes.json", "w") as archivo:
        json.dump (lotes, archivo, indent=4)

def guardar_movimientos():
    hacer_backup("data/movimientos.json")
    with open("data/movimientos.json", "w") as archivo:
        json.dump (movimientos, archivo, indent=4)

def guardar_ventas():
    hacer_backup("data/ventas.json")
    with open("data/ventas.json", "w") as archivo:
        json.dump (ventas, archivo, indent=4)

productos = cargar_productos()
lotes = cargar_lotes()
movimientos = cargar_movimientos()
ventas = cargar_ventas()

def iniciar_sesion():
    print("============ INICIO DE SESION ==================")
    print("1. OPERADOR")
    print("2. INSRUCTOR")
    while True:
        try:
            opcion = int(input("Seleccione su rol: "))
            if opcion == 1:
                return "OPERADOR"
            elif opcion == 2:
                return "INSTRUCTOR"
            else:
                print("Opcion Invalida")
        except ValueError:
            print("Ingrese un numero valido")

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

    costo_unitario = input("Ingrese el costo unitario del producto: ").strip()
    if costo_unitario == "":
        print("El costo unitario no puede quedar vacio")
        return
    try:
        costo_numero = int(costo_unitario)
        if costo_numero < 0:
            print("El costo unitario no puede ser negativo")
            return
    except ValueError:
        print("El costo unitario debe ser un numero valido")
        return

    producto = {
        "codigo":codigo,
        "nombre":nombre,
        "categoria":categoria,
        "unidad":unidad,
        "precio":precio_numero,
        "stock_minimo":stock,
        "activo":True,
        "costo_unitario": costo_numero
    }
    productos.append(producto)
    print(f"Producto {codigo} registrado correctamente")

def consultar_productos():
    if not productos:
        print("No existen productos registrados")
        return
    print(" ")
    print(f"| {"Codigo":<12} | {"Nombre":<12} | {"Categoria":<12} | {"Unidad":<12} |  {"Precio":<12} | {"Min_stock":<12} | {"Activo":<12} |")
    print("-" * 77)
    for producto in productos:
        print(f"| {producto['codigo']:<12} | {producto['nombre']:<12} | {producto['categoria']:<12} | {producto['unidad']:<12} | ${producto['precio']:<12} | {producto['stock_minimo']:<12} | {producto['activo']:<12} |")
        print(" ")

def consultar_productos_activos():
    if not productos:
        print("No existen productos registrados")
        return

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
        return

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
        return

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

    nuevo_costo = input(f"Costo unitario [{resultado['costo_unitario']}]: ").strip()
    if nuevo_costo != "":
        try:
            costo_numero = int(nuevo_costo)
            if costo_numero < 0:
                print("El costo no puede ser negativo, no se actualizo")
            else:
                resultado["costo_unitario"] = costo_numero
        except ValueError:
            print("Costo invalido, no se actualizo")

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

def generar_id_venta():
    numero = len(ventas) + 1
    return f"V{numero:04d}"

def registrar_venta():
    if not productos:
        print("No existen productos registrados")
        return

    submenuVentas()
    items = []

    print("======PRODUCTOS======")
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

    while True:
        codigo = input("Codigo del producto (o FIN para terminar): ").strip().upper()
        if codigo == "FIN":
            break

        encontrado = None
        for producto in productos:
            if producto['codigo'] == codigo:
                encontrado = producto
                break

        if encontrado is None:
            print("No existe un producto con ese codigo")
            continue

        if encontrado['activo'] == False:
            print("El producto esta inactivo, no se puede vender")
            continue

        try:
            cantidad = int(input("Cantidad a vender: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor que 0")
                continue
        except ValueError:
            print("La cantidad debe ser un numero entero")
            continue

        ya_agregado_en_esta_venta = 0
        for item in items:
            if item['codigo'] == codigo:
                ya_agregado_en_esta_venta = ya_agregado_en_esta_venta + item['cantidad']

        stock_disponible = calcular_stock(codigo) - ya_agregado_en_esta_venta
        if cantidad > stock_disponible:
            print(f"Stock insuficiente. Disponible: {stock_disponible}")
            continue

        item = {
            "codigo": codigo,
            "cantidad": cantidad,
            "precio_unitario": encontrado['precio']
        }
        items.append(item)
        print(f"Agregado: {cantidad} x {encontrado['nombre']}")

    if not items:
        print("La venta debe contener al menos un item valido. Venta cancelada")
        return

    total = 0
    for item in items:
        total = total + (item['cantidad'] * item['precio_unitario'])

    venta = {
        "id": generar_id_venta(),
        "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "items": items,
        "total": total
    }
    ventas.append(venta)

    for item in items:
        movimiento = {
            "id": generar_id_movimiento(),
            "producto_codigo": item['codigo'],
            "tipo": "SALIDA",
            "cantidad": item['cantidad'],
            "motivo": f"Venta {venta['id']}",
            "fecha": venta['fecha']
        }
        movimientos.append(movimiento)
    guardar_movimientos()

    print(" ")
    print(f"Venta {venta['id']} registrada correctamente. Total: ${total}")
    print(" ")

def consultar_ventas():
    if not ventas:
        print("No existen ventas registradas")
        return

    print("=========================HISTORIAL DE VENTAS=========================")
    print(" ")
    for venta in ventas:
        print(f"Venta {venta['id']} | Fecha: {venta['fecha']} | Total: ${venta['total']}")
        for item in venta['items']:
            print(f"    - {item['codigo']}: {item['cantidad']} x ${item['precio_unitario']}")
        print(" ")

def consultar_ventas_fecha(fecha_inicio, fecha_fin):
    encontrados = False
    for venta in ventas:
        fecha_venta = venta['fecha'][:10]
        if fecha_inicio <= fecha_venta <= fecha_fin:
            encontrados = True
            print(f"Venta {venta['id']} | Fecha: {venta['fecha']} | Total: ${venta['total']}")
            for item in venta['items']:
                print(f"    - {item['codigo']}: {item['cantidad']} x ${item['precio_unitario']}")
            print(" ")
    if not encontrados:
        print("No hay ventas en ese rango de fechas")


def mostrar_alertas():
    if not productos:
        print("No existen productos registrados")
        return

    encontrados = False
    for producto in productos:
        if producto['activo'] == True:
            stock_actual = calcular_stock(producto['codigo'])
            if stock_actual <= producto['stock_minimo']:
                if not encontrados:
                    print("=======================PRODUCTOS EN ALERTA DE STOCK BAJO=======================")
                    print(" ")
                    print(f"| {'Codigo':<10} | {'Nombre':<15} | {'Stock actual':<14} | {'Stock minimo':<14} |")
                    print("-" * 65)
                    encontrados = True
                print(f"| {producto['codigo']:<10} | {producto['nombre']:<15} | {stock_actual:<14} | {producto['stock_minimo']:<14} |")
                print(" ")

    if encontrados == False:
        print("No hay productos en estado de alerta")
        print(" ")

def reporte_inventario():
    if not productos:
        print("No existen productos registrados")
        return

    print(" ")
    print(f"| {'Codigo':<10} | {'Nombre':<15} | {'Stock':<8} | {'Precio':<10} | {'Valor total':<12} |")
    print("-" * 65)
    valor_total_inventario = 0
    for producto in productos:
        if producto['activo'] == True:
            stock_actual = calcular_stock(producto['codigo'])
            valor = stock_actual * producto['precio']
            valor_total_inventario = valor_total_inventario + valor
            print(f"| {producto['codigo']:<10} | {producto['nombre']:<15} | {stock_actual:<8} | ${producto['precio']:<9} | ${valor:<11} |")
    print("-" * 65)
    print(f"Valor total del inventario (a precio de venta): ${valor_total_inventario}")
    print(" ")

def reporte_ventas():
    if not ventas:
        print("No existen ventas registradas")
        return

    numero_ventas = len(ventas)
    unidades_vendidas = 0
    ingresos_totales = 0

    for venta in ventas:
        ingresos_totales = ingresos_totales + venta['total']
        for item in venta['items']:
            unidades_vendidas = unidades_vendidas + item['cantidad']

    print("============REPORTE DE VENTAS===============")
    print(" ")
    print(f"Numero de ventas: {numero_ventas}")
    print(f"Unidades vendidas: {unidades_vendidas}")
    print(f"Ingresos acumulados: ${ingresos_totales}")
    print(" ")

def reporte_ranking():
    if not ventas:
        print("No existen ventas registradas")
        return

    cantidad_por_producto = {}
    for venta in ventas:
        for item in venta['items']:
            codigo = item['codigo']
            if codigo in cantidad_por_producto:
                cantidad_por_producto[codigo] = cantidad_por_producto[codigo] + item['cantidad']
            else:
                cantidad_por_producto[codigo] = item['cantidad']

    ranking = sorted(cantidad_por_producto.items(), key=lambda x: x[1], reverse=True)
    top3 = ranking[:3]

    print(" ")
    print("Top 3 productos con mayor cantidad vendida:")
    posicion = 1
    for codigo, cantidad in top3:
        print(f"{posicion}. {codigo} - {cantidad} unidades vendidas")
        posicion = posicion + 1
    print(" ")

def reporte_utilidad():
    if not ventas:
        print("No existen ventas registradas")
        return

    utilidad_total = 0
    for venta in ventas:
        for item in venta['items']:
            costo_producto = 0
            for producto in productos:
                if producto['codigo'] == item['codigo']:
                    costo_producto = producto['costo_unitario']
            utilidad_item = (item['precio_unitario'] - costo_producto) * item['cantidad']
            utilidad_total = utilidad_total + utilidad_item

    print(" ")
    print(f"La utilidad estimada acumulada de todas las ventas es de: ${utilidad_total}")
    print(" ")

def registrar_devolucion():
    if not ventas:
        print("No existen ventas registradas")
        return

    id_venta = input("Ingrese el ID de la venta: ").strip().upper()

    venta_encontrada = None
    for venta in ventas:
        if venta['id'] == id_venta:
            venta_encontrada = venta
            break

    if venta_encontrada is None:
        print("No existe una venta con ese ID")
        return

    codigo = input("Ingrese el codigo del producto a devolver: ").strip().upper()

    item_encontrado = None
    for item in venta_encontrada['items']:
        if item['codigo'] == codigo:
            item_encontrado = item
            break

    if item_encontrado is None:
        print("Ese producto no esta en esa venta")
        return

    try:
        cantidad = int(input(f"Cantidad a devolver (maximo {item_encontrado['cantidad']}): "))
        if cantidad <= 0 or cantidad > item_encontrado['cantidad']:
            print("Cantidad invalida")
            return
    except ValueError:
        print("La cantidad debe ser un numero entero")
        return

    movimiento = {
        "id": generar_id_movimiento(),
        "producto_codigo": codigo,
        "tipo": "ENTRADA",
        "cantidad": cantidad,
        "motivo": f"Devolucion venta {id_venta}",
        "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    movimientos.append(movimiento)
    guardar_movimientos()

    print(" ")
    print(f"Devolucion registrada correctamente. Se genero la entrada {movimiento['id']}")
    print(" ")

def exportar_inventario_csv():
    if not productos:
        print("No existen productos registrados")
        return

    with open("data/reporte_inventario.csv", "w", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Codigo", "Nombre", "Categoria", "Stock", "Precio", "Valor total"])
        for producto in productos:
            if producto['activo'] == True:
                stock_actual = calcular_stock(producto['codigo'])
                valor = stock_actual * producto['precio']
                escritor.writerow([producto['codigo'], producto['nombre'], producto['categoria'], stock_actual, producto['precio'], valor])

    print(" ")
    print("Reporte exportado correctamente en data/reporte_inventario.csv")
    print(" ")

def main():
    rol = iniciar_sesion()
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
                            gestionar_estado_lote()
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
            case 4:
                registrar_venta()
                guardar_ventas()
            case 5:
                filtro = input("Filtrar por rango de fechas? (s/n): ").strip().lower()
                if filtro =="s" or filtro == "si":
                    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ").strip()
                    fecha_fin = input("Fecha fin (YYYY-MM-DD): ").strip()
                    consultar_ventas_fecha(fecha_inicio, fecha_fin)
                else:
                    consultar_ventas()
                    
            case 6:
                mostrar_alertas()
            case 7:
                if rol != "INSTRUCTOR":
                    print("====================================================================")
                    print("= ACCESO RESTRINGIDO: SOLO EL ROL DE INSTRUCTOR PUEDE VER REPORTES =")
                    print("====================================================================")
                    continue
                control5 = True
                while (control5):
                    submenuReportes()
                    try:
                        opc5 = int(input("Seleccione una opcion: "))
                    except ValueError:
                        print("Ingrese una opcion valida")
                        continue
                    match(opc5):
                        case 1:
                            reporte_inventario()
                        case 2:
                            reporte_ventas()
                        case 3:
                            reporte_ranking()
                        case 4:
                            reporte_utilidad()
                        case 5:
                            exportar_inventario_csv()
                        case 0:
                            break
            case 8:
                if rol != "INSTRUCTOR":
                    print("=============================================================================")
                    print("= ACCESO RESTRINGIDO: SOLO EL TOL DE INSTRUCTOR PUEDE REALIZAR DEVOLUCIONES =")
                    print("=============================================================================")
                registrar_devolucion()
       
            case 0:
                print("Ha salido del sistema correctamente")
                break

main()