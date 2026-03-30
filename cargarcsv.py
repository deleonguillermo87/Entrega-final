import csv

def cargar_csv(ruta):
    inventario = []
    errores = 0

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            # Validar encabezado
            encabezado_esperado = ["nombre", "precio", "cantidad"]
            if lector.fieldnames != encabezado_esperado:
                print("Error: El encabezado del archivo no es válido.")
                return []

            for fila in lector:
                try:
                    # Validar columnas
                    if len(fila) != 3:
                        errores += 1
                        continue

                    nombre = fila["nombre"]

                    precio = float(fila["precio"])
                    cantidad = int(fila["cantidad"])

                    # Validar no negativos
                    if precio < 0 or cantidad < 0:
                        errores += 1
                        continue

                    producto = {
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    }

                    inventario.append(producto)

                except (ValueError, KeyError):
                    errores += 1

        print(f"Productos cargados: {len(inventario)}")
        print(f"Filas inválidas omitidas: {errores}")

        return inventario

    except FileNotFoundError:
        print("Error: El archivo no existe.")
        return []
    except UnicodeDecodeError:
        print("Error: Problema de codificación del archivo.")
        return []
    except Exception as e:
        print(f"Error inesperado: {e}")
        return []
