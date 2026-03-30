def mostrar_estadisticas(inventario):
    if len(inventario) == 0:
        print("\nNo hay productos para calcular estadisticas.")
        return

    total = len(inventario)
    suma_cantidad = 0

    producto_mas_caro = inventario[0]
    producto_mayor_stock = inventario[0]

    subtotal = lambda p: p["precio"] * p["cantidad"]

    valor_total = sum(map(subtotal, inventario))

    for p in inventario:
        suma_cantidad = suma_cantidad + p["cantidad"]

        if p["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = p

        if p["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = p

    print("\n=== ESTADISTICAS ===")
    print("Total de productos diferentes:", total)
    print("Total de unidades en stock:", suma_cantidad)
    print("Valor total del inventario:", valor_total)
    print("Producto mas caro:", producto_mas_caro["nombre"], "-", producto_mas_caro["precio"])
    print("Producto con mayor stock:", producto_mayor_stock["nombre"], "-", producto_mayor_stock["cantidad"])
