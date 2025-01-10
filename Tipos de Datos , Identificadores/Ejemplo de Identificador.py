print("Semana #5")
print("Ejemplo de Identificadores")

# Buen identificador para una variable que almacena la lista de productos en inventario
lista_productos = ["Laptop", "Smartphone", "Tablet"]

# Buen identificador para una función que agrega un producto al inventario
def agregar_producto(inventario, producto):
    inventario.append(producto)
    return inventario

# Buen identificador para una variable que almacena el nombre del producto a agregar
nuevo_producto = "Auriculares"

# Uso de los identificadores en un contexto de código
print("Inventario inicial:", lista_productos)
lista_productos = agregar_producto(lista_productos, nuevo_producto)
print("Inventario actualizado:", lista_productos)
