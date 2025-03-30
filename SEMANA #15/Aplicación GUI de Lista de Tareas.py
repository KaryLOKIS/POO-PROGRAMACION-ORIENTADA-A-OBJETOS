print("Semana #15 Lista de Tareas")

import tkinter as tk
from tkinter import messagebox

# Función para añadir una nueva tarea
def add_task(event=None):
    # Obtiene el texto de la entrada y elimina espacios en blanco
    task = entry_task.get().strip()
    if task:
        # Añade la tarea al Listbox
        listbox_tasks.insert(tk.END, task)
        # Limpia el campo de entrada
        entry_task.delete(0, tk.END)
    else:
        # Muestra una advertencia si el campo está vacío
        messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

# Función para marcar una tarea como completada
def mark_completed():
    try:
        # Obtiene el índice de la tarea seleccionada
        selected_index = listbox_tasks.curselection()[0]
        # Obtiene el texto de la tarea seleccionada
        task = listbox_tasks.get(selected_index)
        # Elimina la tarea actual de la lista
        listbox_tasks.delete(selected_index)
        # Añade la tarea con un ✔ indicando que está completada
        listbox_tasks.insert(selected_index, f"✔ {task}")
    except IndexError:
        # Muestra una advertencia si no hay tarea seleccionada
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

# Función para eliminar una tarea seleccionada
def delete_task():
    try:
        # Obtiene el índice de la tarea seleccionada
        selected_index = listbox_tasks.curselection()[0]
        # Elimina la tarea de la lista
        listbox_tasks.delete(selected_index)
    except IndexError:
        # Muestra una advertencia si no hay tarea seleccionada
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

# Crear un campo de entrada para nuevas tareas
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=10)
# Permitir añadir tareas presionando la tecla Enter
entry_task.bind("<Return>", add_task)

# Crear un botón para añadir tareas con color
btn_add = tk.Button(root, text="Añadir Tarea", command=add_task, bg="lightblue", fg="black")
btn_add.pack()

# Crear un Listbox para mostrar las tareas
listbox_tasks = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
listbox_tasks.pack(pady=10)

# Crear un botón para marcar tareas como completadas con color
btn_complete = tk.Button(root, text="Marcar como Completada", command=mark_completed, bg="lightgreen", fg="black")
btn_complete.pack()

# Crear un botón para eliminar tareas con color
btn_delete = tk.Button(root, text="Eliminar Tarea", command=delete_task, bg="lightcoral", fg="black")
btn_delete.pack()

# Ejecutar la aplicación
root.mainloop()
