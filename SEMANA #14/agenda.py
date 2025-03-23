print("Semana #14")

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Crear el Frame principal para la aplicación
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(padx=10, pady=10)

        # Título de la aplicación
        self.title_label = tk.Label(self.main_frame, text="Agenda Personal", font=("Arial", 16))
        self.title_label.grid(row=0, columnspan=3, pady=10)

        # Etiquetas y campos de entrada
        self.date_label = tk.Label(self.main_frame, text="Fecha:")
        self.date_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.date_entry = DateEntry(self.main_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.grid(row=1, column=1, padx=10, pady=5)

        self.time_label = tk.Label(self.main_frame, text="Hora:")
        self.time_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.time_entry = tk.Entry(self.main_frame)
        self.time_entry.grid(row=2, column=1, padx=10, pady=5)

        self.desc_label = tk.Label(self.main_frame, text="Descripción:")
        self.desc_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.desc_entry = tk.Entry(self.main_frame)
        self.desc_entry.grid(row=3, column=1, padx=10, pady=5)

        # Botones
        self.add_button = tk.Button(self.main_frame, text="Agregar Evento", command=self.add_event)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(self.main_frame, text="Eliminar Evento Seleccionado", command=self.delete_event)
        self.delete_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.quit_button = tk.Button(self.main_frame, text="Salir", command=root.quit)
        self.quit_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Crear TreeView para mostrar eventos
        self.tree = ttk.Treeview(self.main_frame, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.grid(row=7, column=0, columnspan=2, pady=10)

        # Lista para almacenar eventos
        self.events = []

    def add_event(self):
        # Obtener los valores de los campos de entrada
        date = self.date_entry.get()
        time = self.time_entry.get()
        description = self.desc_entry.get()

        # Verificar de campos
        if date and time and description:
            # Agregar el evento a la lista
            self.events.append((date, time, description))

            # Actualizar el Treeview
            self.tree.insert("", "end", values=(date, time, description))

            # Limpiar los campos de entrada
            self.date_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Todos los campos deben ser llenados.")

    def delete_event(self):
        # Obtener el item seleccionado en el Treeview
        selected_item = self.tree.selection()

        if selected_item:
            # Confirmar eliminación
            result = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar este evento?")
            if result:
                # Eliminar el evento de la lista
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un evento para eliminar.")

if __name__ == "__main__":
    # Crear la ventana principal
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
