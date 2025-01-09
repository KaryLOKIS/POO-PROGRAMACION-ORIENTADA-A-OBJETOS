#Ejemplo #3
print("SISTEMA DE TIENDA")

class Producto:
    def __init__(self, nombre, precio, cantidad):
        """
        Inicializa un producto con su nombre, precio y cantidad en stock.
        """
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio unitario
        self.cantidad = cantidad  # Cantidad en stock

    def __str__(self):
        """Devuelve una representación en texto del producto."""
        return f"{self.nombre} - ${self.precio}"

class Carrito:
    def __init__(self):
        """Inicializa un carrito de compras vacío."""
        self.productos = []  # Lista de productos agregados al carrito

    def agregar_producto(self, producto):
        """Agrega un producto al carrito."""
        self.productos.append(producto)

    def total(self):
        """Calcula el costo total de los productos en el carrito."""
        return sum(p.precio for p in self.productos)

class Cliente:
    def __init__(self, nombre):
        """
        Inicializa un cliente con su nombre y un carrito de compras vacío.
        """
        self.nombre = nombre  # Nombre del cliente
        self.carrito = Carrito()  # Asigna un nuevo carrito de compras al cliente

    def comprar(self):
        """
        Calcula el total de la compra y limpia el carrito.
        """
        total = self.carrito.total()  # Obtiene el total del carrito
        print(f"{self.nombre} compró productos por un total de ${total}.")
        self.carrito.productos.clear()  # Limpia el carrito después de la compra

# Crear productos
producto1 = Producto("Camiseta", 20, 10)
producto2 = Producto("Pantalón", 30, 5)

# Crear cliente y agregar productos al carrito
cliente = Cliente("Juan Gómez")
cliente.carrito.agregar_producto(producto1)
cliente.carrito.agregar_producto(producto2)

# Finalizar la compra
cliente.comprar()
