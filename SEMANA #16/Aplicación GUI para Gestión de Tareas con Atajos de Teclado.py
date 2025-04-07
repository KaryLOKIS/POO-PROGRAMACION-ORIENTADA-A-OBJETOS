print("Semana #16")
print("Gestion de Tareas con Atajos de Teclado")

import tkinter as tk
from tkinter import messagebox

# Clase principal de la aplicación
class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas Pendientes")
        self.root.geometry("450x500")
        self.root.configure(bg="#f0f8ff")  # Fondo azul claro

        # Lista para almacenar tareas
        self.tasks = []

        # Campo de entrada
        self.entry = tk.Entry(self.root, font=('Arial', 14), bg="#ffffff", fg="#000000")
        self.entry.pack(pady=10, padx=10, fill=tk.X)
        self.entry.focus()

        # Botón para añadir tarea
        self.add_button = tk.Button(self.root, text="➕ Añadir Tarea", command=self.add_task,
                                    bg="#4CAF50", fg="white", font=("Arial", 12))
        self.add_button.pack(pady=5)

        # Botón para marcar tarea completada
        self.complete_button = tk.Button(self.root, text="✔ Marcar como Completada", command=self.mark_completed,
                                         bg="#2196F3", fg="white", font=("Arial", 12))
        self.complete_button.pack(pady=5)

        # Botón para eliminar tarea
        self.delete_button = tk.Button(self.root, text="🗑 Eliminar Tarea", command=self.delete_task,
                                       bg="#f44336", fg="white", font=("Arial", 12))
        self.delete_button.pack(pady=5)

        # Listbox para mostrar las tareas
        self.task_listbox = tk.Listbox(self.root, font=('Arial', 12), selectmode=tk.SINGLE,
                                       bg="#fffaf0", fg="#000000", selectbackground="#a8dadc")
        self.task_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Enlace de teclas (atajos)
        self.entry.bind("<Return>", lambda event: self.add_task())       # Añadir con Enter
        self.root.bind("<c>", lambda event: self.mark_completed())       # Marcar completada con 'C'
        self.root.bind("<d>", lambda event: self.delete_task())          # Eliminar con 'D'
        self.root.bind("<Delete>", lambda event: self.delete_task())     # Eliminar con tecla Delete
        self.root.bind("<Escape>", lambda event: self.root.quit())       # Salir con Escape

    # Añadir tarea
    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.tasks.append({"text": task, "completed": False})
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Por favor, escribe una tarea.")

    # Marcar como completada
    def mark_completed(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_listbox()
        else:
            messagebox.showwarning("Sin selección", "Selecciona una tarea primero.")

    # Eliminar tarea
    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_listbox()
        else:
            messagebox.showwarning("Sin selección", "Selecciona una tarea primero.")

    # Actualizar visualmente el Listbox
    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display = f"[✔] {task['text']}" if task["completed"] else f"[ ] {task['text']}"
            self.task_listbox.insert(tk.END, display)

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
