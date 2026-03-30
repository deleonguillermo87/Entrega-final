def buscar_producto(inventario, nombre_buscado):
    for producto in inventario:
        if producto["nombre"] == nombre_buscado:
            return producto
    return None
