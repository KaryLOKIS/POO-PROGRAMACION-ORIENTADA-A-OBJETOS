print("SEMANA #6")
print("Clases, objetos, herencia, encapsulamiento y polimorfismo")

# Clase base que representa un Animal
class Animal:
    def __init__(self, nombre, especie, edad):
        # Atributos encapsulados
        self.__nombre = nombre
        self.__especie = especie
        self.__edad = edad

    # Métodos para acceder y modificar atributos encapsulados
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_especie(self):
        return self.__especie

    def get_edad(self):
        return self.__edad

    # Método que puede ser sorbreescrito
    def emitir_sonido(self):
        return "Sonido genérico de un animal"

    def __str__(self):
        return f"{self.__especie.capitalize()} llamado {self.__nombre}, {self.__edad} años."


# Clase derivada que representa al animal Perro
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Llamar al constructor de la clase base
        super().__init__(nombre, "perro", edad)
        self.raza = raza  # Atributo específico de la clase derivada

    # Sobreescritura de un método (polimorfismo)
    def emitir_sonido(self):
        return "Guau"

    def __str__(self):
        return f"Perro de raza {self.raza}, {super().__str__()}"


# Clase derivada que representa el animal Gato
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        # Llamamos al constructor de la clase base
        super().__init__(nombre, "gato", edad)
        self.color = color  # Atributo específico de la clase derivada

    # Sobreescritura de un método (polimorfismo)
    def emitir_sonido(self):
        return "Miau"

    def __str__(self):
        return f"Gato de color {self.color}, {super().__str__()}"


# Función principal para demostrar el programa
def main():
    # Crear instancias de las clases
    perro1 = Perro("Rex", 5, "Labrador")
    gato1 = Gato("Luna", 3, "Blanco")

    # Mostramos información y sonidos de los animales como el perro y el gato
    print(perro1)
    print(perro1.emitir_sonido())

    print(gato1)
    print(gato1.emitir_sonido())

    # Demostración de encapsulación: accedemos y modificamos atributos privados
    print(f"Nombre original del perro: {perro1.get_nombre()}")
    perro1.set_nombre("Max")
    print(f"Nombre modificado del perro: {perro1.get_nombre()}")


if __name__ == "__main__":
    main()
