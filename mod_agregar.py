def agregar_producto(inventario):
    print("que producto desea registrar")

    while True:
        nombre = input("Ingrese el nombre del producto: ")

        if not nombre:
            print("error el nombre no puede estar vacido")

        elif not nombre.isalpha():
            print("error solo debe tener letras ")

        else:
            break

    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                print(" ingresar valores correctos")
            else:
                break
        except ValueError:
            print("Error: Debe ingresar un número válido para el precio.")

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad disponible: "))
            if cantidad < 0:
                print(" ingresar valores correctos")
            else:
                break
        except ValueError:
            print("Error: Debe ingresar un número entero válido para la cantidad.")

    producto = {
      "nombre": nombre, 
      "precio": precio, 
      "cantidad": cantidad
      }
    inventario.append(producto)

    print("Producto agregado con exito!")
