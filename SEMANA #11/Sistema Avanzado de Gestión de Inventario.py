print("Semana #11")
print("Sistema Avanzado de Gestión de Inventario")

import json


# Definición de la clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # ID único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad en stock
        self.precio = precio  # Precio unitario

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad  # Actualiza la cantidad del producto

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio  # Actualiza el precio del producto

    def to_dict(self):
        # Convierte el objeto Producto en un diccionario para facilitar el almacenamiento
        return {
            "id": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }


# Definición de la clase Inventario
class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.productos = {}  # Diccionario para almacenar productos
        self.archivo = archivo  # Nombre del archivo de almacenamiento
        self.cargar_desde_archivo()  # Carga los datos desde el archivo al iniciar

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        # Agrega un producto al inventario si el ID no existe
        if id_producto in self.productos:
            print("Error: ID ya existente.")
        else:
            self.productos[id_producto] = Producto(id_producto, nombre, cantidad, precio)
            self.guardar_en_archivo()  # Guarda los cambios en el archivo

    def eliminar_producto(self, id_producto):
        # Elimina un producto por su ID si existe
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        # Actualiza la cantidad o el precio de un producto
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                self.productos[id_producto].actualizar_precio(nuevo_precio)
            self.guardar_en_archivo()
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        # Busca un producto por su nombre (sin distinguir mayúsculas/minúsculas)
        for producto in self.productos.values():
            if producto.nombre.lower() == nombre.lower():
                return producto.to_dict()
        return None

    def mostrar_inventario(self):
        # Muestra todos los productos en el inventario
        return [producto.to_dict() for producto in self.productos.values()]

    def guardar_en_archivo(self):
        # Guarda los datos del inventario en un archivo JSON
        with open(self.archivo, "w") as f:
            json.dump({id_p: p.to_dict() for id_p, p in self.productos.items()}, f)

    def cargar_desde_archivo(self):
        # Carga los datos del inventario desde un archivo JSON
        try:
            with open(self.archivo, "r") as f:
                datos = json.load(f)
                self.productos = {id_p: Producto(**p) for id_p, p in datos.items()}
        except FileNotFoundError:
            self.productos = {}  # Si el archivo no existe, inicia un inventario vacío


# Interfaz de Usuario
if __name__ == "__main__":
    inventario = Inventario()

    # Agregar productos de ejemplo
    inventario.agregar_producto("001", "Pan", 50, 0.50)
    inventario.agregar_producto("002", "Leche", 30, 1.20)
    inventario.agregar_producto("003", "Huevos", 20, 2.50)

    while True:
        print("\nMenú de Inventario")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_p = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(id_p, nombre, cantidad, precio)
        elif opcion == "2":
            id_p = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_p)
        elif opcion == "3":
            id_p = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            inventario.actualizar_producto(id_p, int(cantidad) if cantidad else None, float(precio) if precio else None)
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            resultado = inventario.buscar_producto(nombre)
            print(resultado if resultado else "Producto no encontrado.")
        elif opcion == "5":
            print(inventario.mostrar_inventario())
        elif opcion == "6":
            break  # Sale del programa
        else:
            print("Opción no válida.")
