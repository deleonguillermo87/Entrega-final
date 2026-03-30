def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print("\nNo hay productos en el inventario aun.")
    else:
        print("\n=== Productos en inventario ===")
        for prod in inventario:
            print(prod["nombre"], "- Precio:", prod["precio"], "- Cantidad:", prod["cantidad"])
