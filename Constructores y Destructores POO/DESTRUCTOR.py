print("SEMANA #7")
print("DESTRUCTOR")

class Archivo:
    def __init__(self, nombre_archivo):
        #Constructor de la clase Archivo.Inicializa el nombre del archivo y abre el archivo para escritura.

        self.nombre_archivo = nombre_archivo
        self.archivo = open(self.nombre_archivo, 'w')  # Abrir el archivo para escritura
        print(f"Archivo '{self.nombre_archivo}' abierto para escritura.")

    def escribir(self, contenido):
        #metodo para escribir en el archivo
        self.archivo.write(contenido)
        print(f"Contenido '{contenido}' escrito en el archivo.")

    def __del__(self):
        #Destructor de la clase Archivo Cierra el archivo automáticamente al destruir el objeto.

        if hasattr(self, 'archivo') and not self.archivo.closed:
            self.archivo.close()  # Cerrar el archivo al finalizar
            print(f"Archivo '{self.nombre_archivo}' cerrado correctamente.")
        else:
            print(f"El archivo '{self.nombre_archivo}' ya estaba cerrado.")


# Crear una instancia de la clase Archivo
archivo1 = Archivo("documento.txt")
archivo1.escribir("Este es un texto de ejemplo para el archivo.")

# Al finalizar, Python automáticamente llamará al destructor cuando el objeto ya no esté en uso
