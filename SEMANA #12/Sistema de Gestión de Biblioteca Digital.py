print("Semana #12: Sistema de Gestión de Biblioteca Digital")

class Libro:
    # Clase que representa un libro en la biblioteca
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla para almacenar título y autor (inmutables)
        self.categoria = categoria  # Categoría del libro
        self.isbn = isbn  # Código ISBN único del libro

    def __str__(self):
        return f"{self.info[0]} de {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    # Clase que representa un usuario de la biblioteca
    def __init__(self, nombre, user_id):
        self.nombre = nombre  # Nombre del usuario
        self.user_id = user_id  # ID único del usuario
        self.libros_prestados = []  # Lista de libros prestados por el usuario

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.user_id}"


class Biblioteca:
    # Clase que gestiona la biblioteca digital
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = set()  # Conjunto para almacenar IDs de usuarios únicos
        self.prestamos = {}  # Diccionario con ID de usuario como clave y lista de libros prestados como valor

    def agregar_libro(self, libro):
        # Añadir un libro a la biblioteca
        self.libros[libro.isbn] = libro
        print(f"Libro añadido: {libro}")

    def quitar_libro(self, isbn):
        # Eliminar un libro de la biblioteca por su ISBN
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        # Registrar un nuevo usuario en la biblioteca
        if usuario.user_id not in self.usuarios:
            self.usuarios.add(usuario.user_id)
            self.prestamos[usuario.user_id] = []
            print(f"Usuario registrado: {usuario}")
        else:
            print("El usuario ya está registrado.")

    def dar_baja_usuario(self, user_id):
        # Eliminar un usuario si no tiene libros prestados
        if user_id in self.usuarios:
            if self.prestamos[user_id]:
                print("El usuario tiene libros pendientes. No se puede dar de baja.")
            else:
                self.usuarios.remove(user_id)
                del self.prestamos[user_id]
                print(f"Usuario con ID {user_id} eliminado.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, user_id, isbn):
        # Prestar un libro a un usuario
        if user_id in self.usuarios and isbn in self.libros:
            self.prestamos[user_id].append(self.libros[isbn])
            print(f"Libro prestado a usuario {user_id}: {self.libros[isbn]}")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, user_id, isbn):
        # Devolver un libro prestado
        if user_id in self.usuarios and isbn in [libro.isbn for libro in self.prestamos[user_id]]:
            self.prestamos[user_id] = [libro for libro in self.prestamos[user_id] if libro.isbn != isbn]
            print(f"Libro con ISBN {isbn} devuelto por usuario {user_id}.")
        else:
            print("No se encontró el préstamo del libro.")

    def buscar_libro(self, clave):
        # Buscar libros por título, autor o categoría
        resultados = [libro for libro in self.libros.values() if clave.lower() in libro.info[0].lower() or clave.lower() in libro.info[1].lower() or clave.lower() in libro.categoria.lower()]
        return resultados if resultados else "No se encontraron resultados."

    def listar_libros_prestados(self, user_id):
        # Mostrar libros prestados a un usuario específico
        if user_id in self.usuarios:
            return self.prestamos[user_id] if self.prestamos[user_id] else "No tiene libros prestados."
        else:
            return "Usuario no encontrado."


# Datos de ejemplo para probar el sistema
biblioteca = Biblioteca()

# Agregar libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "12345")
libro2 = Libro("1984", "George Orwell", "Distopía", "67890")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Ana Pérez", "U001")
usuario2 = Usuario("Carlos Gómez", "U002")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar y devolver libros
biblioteca.prestar_libro("U001", "12345")
biblioteca.listar_libros_prestados("U001")
biblioteca.devolver_libro("U001", "12345")

# Buscar libros
print(biblioteca.buscar_libro("1984"))
