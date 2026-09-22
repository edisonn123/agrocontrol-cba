# AgroControl CBA

Sistema monolítico en Python para gestionar productos, lotes productivos,
movimientos de inventario y ventas de una unidad agropecuaria del CBA.

## Estructura
agrocontrol_cba/
├── main.py
├── data/ (productos.json, lotes.json, movimientos.json, ventas.json)
├── README.md
└── .gitignore

## Funciones
- Registrar Productos
- Guardar Productos
- Consultar productos
- Consultar productos activos
- Consultar productos con codigo
- Consultar productos con nombre
- Actualizar producto
- Gestionar estado de producto
- Registrar lote
- Guardar lotes
- Sembrar lote
- Cosechar lote
- Gestionar estado de lote
- Consultar lotes
- Registrar entrada manual
- Guardar movimientos
- Registrar salida manual
- Consultar movimientos
- Registrar venta
- Guardar ventas
- Consultar ventas
- Mostrar alertas
- Reporte de inventario
- Reporte de ventas

## Reglas principales
- Códigos de producto y lote son únicos y se guardan en mayúscula.
- El stock se calcula siempre a partir de los movimientos de inventario.
- Un producto inactivo no puede usarse en nuevos lotes ni ventas.
- Un lote solo puede cosecharse una vez, y al hacerlo genera entrada automática.
- Un lote cancelado se puede reactivar; uno cosechado no puede cambiar de estado.
- Ninguna salida o venta puede dejar el stock en negativo.

## Ejecución
python main.py

## Autor(es)
[Edison Lopez] - [3410645 - Programacion de software - CBA]