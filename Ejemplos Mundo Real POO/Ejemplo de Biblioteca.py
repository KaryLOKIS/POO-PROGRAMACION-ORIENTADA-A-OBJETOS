#Ejemplo #2
print("Biblioteca")

class Libro:
    def __init__(self, titulo, autor):
        """
        Inicializa un libro con su título, autor y disponibilidad.
        Por defecto, el libro está disponible.
        """
        self.titulo = titulo  # Título del libro
        self.autor = autor  # Autor del libro
        self.disponibilidad = True  # Disponibilidad del libro (True = disponible)

    def tomar_prestado(self):
        """
        Permite tomar prestado el libro si está disponible.
        """
        if self.disponibilidad:
            self.disponibilidad = False
            return True
        return False

    def devolver(self):
        """
        Devuelve el libro, marcándolo como disponible nuevamente.
        """
        self.disponibilidad = True

class Usuario:
    def __init__(self, nombre):
        """
        Inicializa un usuario con su nombre y una lista vacía de libros prestados.
        """
        self.nombre = nombre  # Nombre del usuario
        self.libros_prestados = []  # Lista de libros prestados por el usuario

    def tomar_libro(self, libro):
        """
        Intenta tomar prestado un libro. Si es exitoso, lo agrega a la lista de libros prestados.
        """
        if libro.tomar_prestado():
            self.libros_prestados.append(libro)
            print(f"{self.nombre} ha tomado prestado '{libro.titulo}'.")
        else:
            print(f"'{libro.titulo}' no está disponible.")

    def devolver_libro(self, libro):
        """
        Devuelve un libro y lo elimina de la lista de libros prestados.
        """
        libro.devolver()
        self.libros_prestados.remove(libro)
        print(f"{self.nombre} ha devuelto '{libro.titulo}'.")

# Crear libros
libro1 = Libro("Python para todos", "Autor1")
libro2 = Libro("Fundamentos de Programación", "Autor2")

# Crear un usuario y realizar préstamos y devoluciones
usuario1 = Usuario("Carlos López")
usuario1.tomar_libro(libro1)
usuario1.devolver_libro(libro1)
