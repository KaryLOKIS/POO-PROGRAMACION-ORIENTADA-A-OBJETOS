print("Semana #13")
print("Creacion de una Aplicacion GIU Básica")

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class SimpleGUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Datos")
        self.root.geometry("400x300")

        # Etiqueta y campo de entrada
        self.label = tk.Label(root, text="Ingrese un dato:")
        self.label.pack(pady=5)

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)

        # Botón para agregar datos
        self.add_button = tk.Button(root, text="Agregar", command=self.add_data, bg="lightgreen", fg="black")
        self.add_button.pack(pady=5)

        # Tabla para mostrar datos
        self.tree = ttk.Treeview(root, columns=("Datos"), show="headings")
        self.tree.heading("Datos", text="Datos ingresados")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        # Botón para limpiar lista
        self.clear_button = tk.Button(root, text="Limpiar", command=self.clear_data, bg="lightcoral", fg="black")
        self.clear_button.pack(pady=5)

    def add_data(self):
        dato = self.entry.get()
        if dato:
            self.tree.insert("", "end", values=(dato,))
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Ingrese un dato antes de agregar.")

    def clear_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)


# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleGUIApp(root)
    root.mainloop()