# 📦 Sistema de Inventario en Python

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Estado](https://img.shields.io/badge/Estado-En%20desarrollo-yellow)
![Licencia](https://img.shields.io/badge/Licencia-MIT-green)

Sistema de gestión de inventario desarrollado en Python desde consola. Permite administrar productos y guardar/cargar datos usando archivos CSV.

---

## 📌 Características

- CRUD completo de productos
- Búsqueda por nombre
- Actualización de precio y cantidad
- Eliminación de productos
- Estadísticas del inventario
- Guardado y carga en CSV
- Código modular

---

## 🧱 Estructura del Proyecto
proyecto_inventario/
│
├── main.py
├── mod_agregar.py
├── mod_mostrar.py
├── mod_buscar.py
├── mod_actualizar.py
├── mod_eliminar.py
├── mod_estadistica.py
├── guardarcsv.py
├── cargarcsv.py
└── datos_csv.csv (opcional)
---

## ⚙️ Requisitos

- Python 3.x
- No necesita librerías externas

---

## ▶️ Cómo ejecutar

```bash
python main.py

🧠 Cómo funciona

El inventario es una lista de diccionarios:
inventario = [
    {"nombre": "Laptop", "precio": 2500, "cantidad": 5},
    {"nombre": "Mouse", "precio": 50, "cantidad": 20}
]

##💾 Persistencia

Guardar CSV

Guarda el inventario en datos_csv.csv

Cargar CSV

Tienes dos opciones:
	•	Sobrescribir inventario
	•	Fusionar datos:
	•	Suma cantidades
	•	Actualiza precios
##📊 Menú
	1.	Agregar producto
	2.	Mostrar inventario
	3.	Buscar producto
	4.	Actualizar producto
	5.	Eliminar producto
	6.	Estadísticas
	7.	Guardar CSV
	8.	Cargar CSV
	9.	Salir
##📌 Notas
	•	El nombre del producto es único
	•	Puedes dejar campos vacíos al actualizar
	•	Maneja validaciones básicas
##👨‍💻 Autor

Proyecto de práctica en Python enfocado en:
	•	Listas y diccionarios
	•	Modularización
	•	Manejo de archivos