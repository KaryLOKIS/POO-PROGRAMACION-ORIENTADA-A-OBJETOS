#SEMANA 3
print("Programacion POO")

class ClimaBase:
    """ Clase base que contiene la funcionalidad esencial para manejar datos del clima."""
    def __init__(self):
        self._temperaturas = []  # Encapsulamiento de las temperaturas

    def agregar_temperatura(self, temperatura):
        """
        Agregamos una temperatura diaria a la lista de temperaturas.

         """
        self._temperaturas.append(temperatura)

    def calcular_promedio(self):
        """
        Calcula el promedio de las temperaturas almacenadas.

        """
        if not self._temperaturas:
            raise ValueError("No hay temperaturas disponibles para calcular el promedio.")
        return sum(self._temperaturas) / len(self._temperaturas)

class ClimaExtendido(ClimaBase):
    """
    codigo de funcionalidad adicional, demostrando herencia.
    """
    def mostrar_temperaturas(self):
        """
        Muestra las temperaturas almacenadas.
        """
        if not self._temperaturas:
            print("No hay temperaturas registradas.")
        else:
            print("Temperaturas ingresadas: ", self._temperaturas)

# Polimorfismo: Creamos diferentes clases para demostrar comportamiento especializado
class ClimaCelsius(ClimaExtendido):
    """
    Clase para manejar temperaturas en grados Celsius.
    """
    def agregar_temperatura(self, temperatura):
        if temperatura < -273.15:
            raise ValueError("La temperatura no puede estar por debajo del cero absoluto en Celsius.")
        super().agregar_temperatura(temperatura)

class ClimaFahrenheit(ClimaExtendido):
    """
    Clase para manejar temperaturas en grados Fahrenheit.
    """
    def agregar_temperatura(self, temperatura):
        if temperatura < -459.67:
            raise ValueError("La temperatura no puede estar por debajo del cero absoluto en Fahrenheit.")
        super().agregar_temperatura(temperatura)

def main_poo():
    print("\n*** Programación Orientada a Objetos ***\n")

    # Crear una instancia de ClimaCelsius
    clima = ClimaCelsius()

    # Agregaremos temperaturas
    temperaturas_celsius = [20.5, 22.0, 21.5, 19.8, 23.1, 20.0, 22.2]
    for temp in temperaturas_celsius:
        clima.agregar_temperatura(temp)

    # Mostramos las temperaturas y calcular el promedio
    clima.mostrar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperaturas en Celsius es: {promedio:.2f} °C")

    # Creamos una instancia de ClimaFahrenheit
    clima_fahrenheit = ClimaFahrenheit()

    # Convertimos las temperaturas a Fahrenheit y agregar
    temperaturas_fahrenheit = [(temp * 9/5) + 32 for temp in temperaturas_celsius]
    for temp in temperaturas_fahrenheit:
        clima_fahrenheit.agregar_temperatura(temp)

    # Mostramos las temperaturas en Fahrenheit y se calculara el promedio
    clima_fahrenheit.mostrar_temperaturas()
    promedio_f = clima_fahrenheit.calcular_promedio()
    print(f"El promedio semanal de temperaturas en Fahrenheit es: {promedio_f:.2f} °F")

if __name__ == "__main__":
    main_poo()


#La Programación Orientada a Objetos (POO) ofrece una solución más robusta y flexible, especialmente cuando el proyecto crece en tamaño y complejidad. Su enfoque modular y organizado, a través de clases y objetos, permite una mayor reutilización del código, escalabilidad y facilidad de mantenimiento
# El encapsulamiento y otros conceptos de la POO, como la herencia y el polimorfismo, permiten realizar cambios sin afectar otras partes del código, lo que facilita tanto la extensión como la corrección del sistema.