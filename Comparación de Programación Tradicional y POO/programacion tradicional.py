#SEMANA 3
print("Programacion Tradicional")
def capturar_temperaturas_diarias():

    """Temperaturas para cada día de la semana."""
    "Colocaremos todos los dias de la semana y asi ver la temperaturas respectivamnente"
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas = [22.5, 24.0, 21.7, 23.5, 25.0, 26.3, 24.8]

    for dia, temp in zip(dias, temperaturas):
        print(f"{dia}: {temp} grados")
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    """Calcula el promedio de temperatura semanal."""
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio

def principal():
    """Función principal para ejecutar el programa sobre las temperaturas de la semana."""
    print("¡Bienvenidos a las Temperaturas Semanales!")
    temperaturas_semanales = capturar_temperaturas_diarias()
    #promediamos las temperaturas de la semana y lo imprimimos
    promedio_semanal = calcular_promedio_semanal(temperaturas_semanales)
    print(f"\nEl promedio semanal de temperaturas es: {promedio_semanal:.2f} grados.")

if __name__ == "__main__":
    principal()

#La Programación Tradicional es un enfoque sencillo y directo, ideal para proyectos pequeños o cuando se busca una solución rápida. Su estructura secuencial y el uso de funciones facilitan el aprendizaje para principiantes, ya que permite implementar soluciones sin complicaciones.