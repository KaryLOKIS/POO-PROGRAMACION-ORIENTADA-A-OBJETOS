print("Semana #10")
print("Manipulacion de archivos y manejo de excepciones")

import os
import json


# Clase que representa un producto en el inventario
class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    # Convierte un objeto Producto en un diccionario para guardarlo en JSON
    def to_dict(self):
        return {"codigo": self.codigo, "nombre": self.nombre, "precio": self.precio, "cantidad": self.cantidad}

    # Crea un objeto Producto a partir de un diccionario
    @staticmethod
    def from_dict(data):
        return Producto(data["codigo"], data["nombre"], data["precio"], data["cantidad"])


# Clase que maneja el inventario de productos
class Inventario:
    ARCHIVO = "inventario.txt"  # Nombre del archivo donde se guardará el inventario

    def __init__(self):
        # Inventario inicial con algunos productos por defecto
        self.productos = {
            "001": Producto("001", "Laptop", 1500.0, 10),
            "002": Producto("002", "Mouse", 25.0, 50),
            "003": Producto("003", "Teclado", 45.0, 30)
        }
        self.cargar_desde_archivo()  # Cargar productos desde el archivo si existe

    # Agrega un nuevo producto al inventario
    def agregar_producto(self, producto):
        if producto.codigo in self.productos:
            print("Error: El producto ya existe.")
        else:
            self.productos[producto.codigo] = producto
            self.guardar_en_archivo()
            print("Producto agregado correctamente.")

    # Actualiza la información de un producto existente
    def actualizar_producto(self, codigo, nombre=None, precio=None, cantidad=None):
        if codigo in self.productos:
            if nombre:
                self.productos[codigo].nombre = nombre
            if precio:
                self.productos[codigo].precio = precio
            if cantidad:
                self.productos[codigo].cantidad = cantidad
            self.guardar_en_archivo()
            print("Producto actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    # Elimina un producto del inventario
    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            self.guardar_en_archivo()
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    # Lista todos los productos en el inventario
    def listar_productos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for producto in self.productos.values():
                print(
                    f"Código: {producto.codigo}, Nombre: {producto.nombre}, Precio: {producto.precio}, Cantidad: {producto.cantidad}")

    # Guarda el inventario en un archivo JSON
    def guardar_en_archivo(self):
        try:
            with open(self.ARCHIVO, "w") as file:
                json.dump([p.to_dict() for p in self.productos.values()], file)
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado: {e}")

    # Carga el inventario desde un archivo JSON
    def cargar_desde_archivo(self):
        if os.path.exists(self.ARCHIVO):
            try:
                with open(self.ARCHIVO, "r") as file:
                    data = json.load(file)
                    self.productos = {p["codigo"]: Producto.from_dict(p) for p in data}
            except FileNotFoundError:
                print("Archivo de inventario no encontrado. Se creará uno nuevo.")
            except json.JSONDecodeError:
                print("Error: Archivo de inventario corrupto. Se procederá con un inventario vacío.")
            except Exception as e:
                print(f"Error inesperado al leer el archivo: {e}")


# Interfaz de usuario en la consola
if __name__ == "__main__":
    inventario = Inventario()
    while True:
        print("\n1. Agregar Producto")
        print("2. Actualizar Producto")
        print("3. Eliminar Producto")
        print("4. Listar Productos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Solicita los datos del nuevo producto al usuario
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            inventario.agregar_producto(Producto(codigo, nombre, precio, cantidad))
        elif opcion == "2":
            # Solicita el código del producto a actualizar y los cambios
            codigo = input("Código del producto a actualizar: ")
            nombre = input("Nuevo nombre (presione enter para omitir): ") or None
            precio = input("Nuevo precio (presione enter para omitir): ")
            precio = float(precio) if precio else None
            cantidad = input("Nueva cantidad (presione enter para omitir): ")
            cantidad = int(cantidad) if cantidad else None
            inventario.actualizar_producto(codigo, nombre, precio, cantidad)
        elif opcion == "3":
            # Solicita el código del producto a eliminar
            codigo = input("Código del producto a eliminar: ")
            inventario.eliminar_producto(codigo)
        elif opcion == "4":
            # Lista todos los productos en el inventario
            inventario.listar_productos()
        elif opcion == "5":
            # Sale del programa
            break
        else:
            print("Opción no válida, intente de nuevo.")
