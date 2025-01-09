print("Ejemplos de Características de la programación orientada a objetos")
print("Semana 5")
print("EJEMPLO DE RESERVA DE UN HOTEL")

class Habitacion:
    def __init__(self, tipo, numero):
        """
        Inicializa una habitación con un tipo, número y estado.
        El estado inicial de la habitación es 'disponible'.
        """
        self.tipo = tipo  # Tipo de la habitación (e.g., doble, suite)
        self.numero = numero  # Número de habitación
        self.estado = "disponible"  # Estado inicial de la habitación

    def reservar(self):
        """Cambia el estado de la habitación a 'ocupada'."""
        self.estado = "ocupada"

    def liberar(self):
        """Cambia el estado de la habitación a 'disponible'."""
        self.estado = "disponible"

class Cliente:
    def __init__(self, nombre, email):
        """
        Inicializa un cliente con su nombre, email y una lista vacía de reservas.
        """
        self.nombre = nombre  # Nombre del cliente
        self.email = email  # Email del cliente
        self.reservas = []  # Lista para almacenar reservas del cliente

    def hacer_reserva(self, habitacion, fechas):
        """
        Reserva una habitación para el cliente si está disponible.
        """
        if habitacion.estado == "disponible":
            habitacion.reservar()  # Cambia el estado de la habitación a 'ocupada'
            reserva = Reserva(self, habitacion, fechas)  # Crea una nueva reserva
            self.reservas.append(reserva)  # Agrega la reserva a la lista del cliente
            print(f"Reserva realizada para {self.nombre} en habitación {habitacion.numero} desde {fechas}.")
        else:
            print(f"La habitación {habitacion.numero} no está disponible.")

class Reserva:
    def __init__(self, cliente, habitacion, fechas):
        """
        Inicializa una reserva con un cliente, una habitación y las fechas de la reserva.
        """
        self.cliente = cliente  # Cliente asociado a la reserva
        self.habitacion = habitacion  # Habitación reservada
        self.fechas = fechas  # Fechas de la reserva

# Ejecución del ejemplo
habitacion1 = Habitacion("doble", 101)
habitacion2 = Habitacion("suite", 102)

cliente1 = Cliente("Juan Pérez", "juan@email.com")
cliente2 = Cliente("Ana Gómez", "ana@email.com")

# Realizar reservas
cliente1.hacer_reserva(habitacion1, "01-02-2025 a 03-02-2025")
cliente2.hacer_reserva(habitacion2, "05-02-2025 a 07-02-2025")
