print("Tecnicas de Prigramacion")
print("Abstraccio,Encapsulacion,Herencia,Polimorfismo")
from abc import ABC, abstractmethod
#ABSTRACCION
# Clase abstracta que define un método que debe implementarse en las clases derivadas
class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass  # Este método debe ser definido por cualquier clase que herede de Animal

# Clase concreta que implementa el método abstracto
class Perro(Animal):
    def hacer_sonido(self):
        print("Guau guau")  # Implementación específica para la clase Perro

# Código principal
if __name__ == "__main__":
    # Crear una instancia de la clase Perro y llamar al método hacer_sonido
    mi_perro = Perro()
    mi_perro.hacer_sonido()

#ENCAPSULACION
# Clase que implementa la encapsulación utilizando atributos privados
class Persona:
    def __init__(self):
        self.__nombre = None  # Atributo privado, no accesible directamente desde fuera de la clase

    # Método para obtener el valor del atributo privado
    def get_nombre(self):
        return self.__nombre

    # Método para asignar un valor al atributo privado
    def set_nombre(self, nombre):
        self.__nombre = nombre

# Código principal
if __name__ == "__main__":
    # Crear una instancia de la clase Persona
    persona = Persona()
    # Establecer un nombre utilizando el método setter
    persona.set_nombre("Juan")
    # Obtener y mostrar el nombre utilizando el método getter
    print("Nombre:", persona.get_nombre())

# HERENCIA
class Vehiculo:
    def encender(self):
        print("El vehículo está encendido.")

# Clase derivada que extiende la funcionalidad de la clase base
class Carro(Vehiculo):
    def conducir(self):
        print("El carro está en movimiento.")

# Código principal
if __name__ == "__main__":
    # Crear una instancia de la clase Carro
    mi_carro = Carro()
    # Llamar al método de la clase base
    mi_carro.encender()
    # Llamar al método de la clase derivada
    mi_carro.conducir()

# POLIMORFISMO
class Figura:
    def dibujar(self):
        print("Dibujando una figura.")  # Método base que puede ser sobrescrito

# Clase derivada que redefine el método de la clase base
class Circulo(Figura):
    def dibujar(self):
        print("Dibujando un círculo.")  # Implementación específica para la clase Circulo

# Código principal
if __name__ == "__main__":
    # Crear una instancia de la clase Circulo, tratándola como una Figura
    figura = Circulo()
    # Llamar al método dibujar, que utiliza la versión redefinida en Circulo
    figura.dibujar()
