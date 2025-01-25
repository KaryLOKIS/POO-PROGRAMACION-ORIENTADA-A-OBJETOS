print("SEMANA #7")
print("CONSTRUCTOR")

class Persona:
    def __init__(self, nombre, edad):
        """
        Constructor de la clase Persona.
        Inicializa el nombre y la edad del objeto Persona.
        """
        self.nombre = nombre   # Atributo nombre de la persona
        self.edad = edad       # Atributo edad de la persona
        print(f"Se ha creado una persona con el nombre: {self.nombre} y edad: {self.edad}")

    def mostrar_informacion(self):
        #metodo para mostrar la informacion d elal persona
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30)

# Usar el metodo para mostrar la informacion
persona1.mostrar_informacion()
