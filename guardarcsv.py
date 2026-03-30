import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    if not inventario:
        print("El inventario está vacío. No hay nada que guardar.")
        return

    fieldnames = ["nombre", "precio", "cantidad"]

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=fieldnames)

            if incluir_header:
                escritor.writeheader()

            for producto in inventario:
                escritor.writerow(producto)

        print(f"Inventario guardado en: {ruta}")

    except PermissionError:
        print("Error: No tienes permisos para escribir en ese archivo.")
    except Exception as e:
        print(f"Error inesperado al guardar: {e}")
