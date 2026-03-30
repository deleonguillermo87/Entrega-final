def eliminar_producto(inventario, nombre_buscado):
    for i in range(len(inventario)):
        if inventario[i]["nombre"] == nombre_buscado:
            inventario.pop(i)
            return True
    return False
