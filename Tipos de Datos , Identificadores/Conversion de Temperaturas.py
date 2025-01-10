print("Semana #5")
print("Conversion de Temperaturas")
"""
Programa para convertir una temperatura en grados Celsius a Fahrenheit y Kelvin.
El programa solicita la temperatura en Celsius, realiza las conversiones y verifica si está por debajo del punto de congelación del agua.
"""

# Función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius: float) -> float:
    """
    Conviertiremos las temperaturas de grados Celsius a Fahrenheit.

    :param celsius: Temperatura en grados Celsius.
    :return: Temperatura convertida a grados Fahrenheit.
    """
    return (celsius * 9/ 5) + 32


# Función para convertir Celsius a Kelvin
def celsius_a_kelvin(celsius: float) -> float:
    """
    Conviertiremos las temperatura de grados Celsius a Kelvin.

    :param celsius: Temperatura en grados Celsius.
    :return: Temperatura convertida a Kelvin.
    """
    return celsius + 273.15


# Bloque principal del programa
if __name__ == "__main__":
    print("CONVERSOR DE TEMPERATURA")
    print("-------------------------")

    # Solicitamos que el usuario que coloque una temperatura en Celsius
    while True:
        try:
            temperatura_celsius = float(input("Ingresa la temperatura en grados Celsius: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")

    # Realizar las conversiones de temperatura
    temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
    temperatura_kelvin = celsius_a_kelvin(temperatura_celsius)

    # Verificar si la temperatura está por debajo del punto de congelación del agua
    es_congelacion = temperatura_celsius < 0  # boolean

    # Mostrar los resultados obtenidos de las conversiones
    print("\nRESULTADOS")
    print(f"Temperatura en Celsius: {temperatura_celsius:.2f}°C")
    print(f"Temperatura en Fahrenheit: {temperatura_fahrenheit:.2f}°F")
    print(f"Temperatura en Kelvin: {temperatura_kelvin:.2f} K")
    if es_congelacion:
        print("La temperatura está por debajo del punto de congelación del agua.")
    else:
        print("La temperatura está por encima del punto de congelación del agua.")
