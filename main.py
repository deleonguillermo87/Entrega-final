import sys
sys.path.append('.')

# Importo funciones de los módulos del sistema
from mod_agregar import agregar_producto
from mod_mostrar import mostrar_inventario
from mod_buscar import *
from mod_eliminar import eliminar_producto
from mod_estadistica import mostrar_estadisticas
from mod_actualizar import actualizar_inventario

# Importo funciones de persistencia CSV
from guardarcsv import guardar_csv
from cargarcsv import cargar_csv


print("=== SISTEMA DE INVENTARIO ===")

# Inventario en memoria
inventario = []

while True:
    print("\nOpciones disponibles:")
    print("1. Agregar un producto")
    print("2. Ver el inventario")
    print("3. Buscar un producto")
    print("4. Actualizar un producto")
    print("5. Eliminar un producto")
    print("6. Calcular estadísticas")
    print("7. Guardar archivo CSV")
    print("8. Cargar archivo CSV")
    print("9. Salir")

    opcion = input("Elige la opción: ")

    # --- OPCIÓN 1 ---
    if opcion == "1":
        agregar_producto(inventario)

    # --- OPCIÓN 2 ---
    elif opcion == "2":
        mostrar_inventario(inventario)

    # --- OPCIÓN 3 ---
    elif opcion == "3":
        nombre = input("Ingresa el nombre del producto: ")
        resultado = buscar_producto(inventario, nombre)

        if resultado:
            print("Producto encontrado:", resultado)
        else:
            print("El producto no existe en el inventario")

    # --- OPCIÓN 4 ---
    elif opcion == "4":
        nombre = input("Ingresa el nombre del producto a actualizar: ")

        while True:
            try:
                nuevo_precio = input("Ingresa el nuevo precio (Enter para mantener): ")
                if nuevo_precio == "":
                    nuevo_precio = None
                else:
                    nuevo_precio = float(nuevo_precio)
                break
            except ValueError:
                print("Error: ingresa un número válido")

        while True:
            try:
                nueva_cantidad = input("Ingresa la nueva cantidad (Enter para mantener): ")
                if nueva_cantidad == "":
                    nueva_cantidad = None
                else:
                    nueva_cantidad = int(nueva_cantidad)
                break
            except ValueError:
                print("Error: ingresa un número válido")

        actualizar_inventario(inventario, nombre, nuevo_precio, nueva_cantidad)

    # --- OPCIÓN 5 ---
    elif opcion == "5":
        nombre = input("Ingresa el nombre del producto a eliminar: ")
        eliminado = eliminar_producto(inventario, nombre)

        if eliminado:
            print("Producto eliminado correctamente")
        else:
            print("El producto no existe")

    # --- OPCIÓN 6 ---
    elif opcion == "6":
        mostrar_estadisticas(inventario)

    # --- OPCIÓN 7: GUARDAR CSV ---
    elif opcion == "7":
        ruta = "datos_csv.csv"
        guardar_csv(inventario, ruta)

    # --- OPCIÓN 8: CARGAR CSV CON VALIDACIONES Y OPCIONES ---
    elif opcion == "8":
        ruta = "datos_csv.csv"
        datos_cargados = cargar_csv(ruta)

        if not datos_cargados:
            print("No se cargaron datos.")
        else:
            opcion_usuario = input("¿Sobrescribir inventario actual? (S/N): ").upper()

            if opcion_usuario == "S":
                inventario = datos_cargados
                print("Inventario reemplazado correctamente.")

            elif opcion_usuario == "N":
                # Fusión por nombre
                for nuevo in datos_cargados:
                    encontrado = False

                    for producto in inventario:
                        if producto["nombre"] == nuevo["nombre"]:
                            # Suma cantidad
                            producto["cantidad"] += nuevo["cantidad"]

                            # Actualiza precio si es diferente
                            producto["precio"] = nuevo["precio"]

                            encontrado = True
                            break

                    # Si no existe, se agrega
                    if not encontrado:
                        inventario.append(nuevo)

                print("Inventario fusionado correctamente.")

            else:
                print("Opción inválida. No se realizaron cambios.")

    # --- OPCIÓN 9 ---
    elif opcion == "9":
        print("Saliendo del sistema...")
        break

    # --- OPCIÓN INVÁLIDA ---
    else:
        print("Opción no válida, intenta de nuevo")
