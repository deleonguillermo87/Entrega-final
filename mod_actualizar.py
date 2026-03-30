# mod_actualizar.py
def actualizar_inventario(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    for producto in inventario:
        # COMPARACIÓN 
        if producto["nombre"].strip().lower() == nombre.strip().lower():

            if nuevo_precio is not None:
                producto["precio"] = nuevo_precio

            if nueva_cantidad is not None:
                producto["cantidad"] = nueva_cantidad

            print("Producto actualizado correctamente")
            return

    print("El producto no existe en el inventario")
