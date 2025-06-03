import tkinter as tk
from tkinter import ttk, messagebox

alumnos = {}

def agregar_alumno():
    nombre = entry_nombre.get().strip()
    nota1 = entry_nota1.get()
    nota2 = entry_nota2.get()

    if not nombre:
        messagebox.showwarning("Falta información", "Debe ingresar el nombre del alumno.")
        return

    try:
        nota1 = int(nota1)
        nota2 = int(nota2)
        if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10):
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Las notas deben estar entre 0 y 10.")
        return

    alumnos[nombre] = [nota1, nota2]
    actualizar_tabla()
    entry_nombre.delete(0, tk.END)
    entry_nota1.delete(0, tk.END)
    entry_nota2.delete(0, tk.END)

def actualizar_tabla():
    for row in tabla.get_children():
        tabla.delete(row)
    for alumno, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        tabla.insert("", tk.END, values=(alumno, notas[0], notas[1], f"{promedio:.2f}"))

def buscar_promedio():
    nombre = entry_busqueda.get().strip()
    if nombre in alumnos:
        notas = alumnos[nombre]
        promedio = sum(notas) / len(notas)
        messagebox.showinfo("Promedio", f"🎓 El promedio de {nombre} es: {promedio:.2f}")
    else:
        messagebox.showerror("No encontrado", "Alumno no encontrado o sin notas.")

# Ventana
root = tk.Tk()
root.title("Gestor de Notas")
root.geometry("700x550")
root.configure(bg="white")

# Fuente y estilos
fuente_titulo = ("Helvetica", 24, "bold")
fuente_texto = ("Helvetica", 12)
color_primario = "#3e6ae1"
color_fondo = "white"
color_borde = "#e5e5e5"

# Título
titulo = tk.Label(root, text="📘 Subir Notas de Alumnos", font=fuente_titulo, bg=color_fondo, fg="black")
titulo.pack(pady=20)

# Formulario
frame_form = tk.Frame(root, bg=color_fondo)
frame_form.pack(pady=10)

tk.Label(frame_form, text="Nombre y Apellido:", font=fuente_texto, bg=color_fondo).grid(row=0, column=0, sticky="e", padx=10, pady=5)
entry_nombre = tk.Entry(frame_form, font=fuente_texto, width=30, bd=1, relief="solid")
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_form, text="Nota 1:", font=fuente_texto, bg=color_fondo).grid(row=1, column=0, sticky="e", padx=10, pady=5)
entry_nota1 = tk.Entry(frame_form, font=fuente_texto, width=10, bd=1, relief="solid")
entry_nota1.grid(row=1, column=1, sticky="w", padx=10, pady=5)

tk.Label(frame_form, text="Nota 2:", font=fuente_texto, bg=color_fondo).grid(row=2, column=0, sticky="e", padx=10, pady=5)
entry_nota2 = tk.Entry(frame_form, font=fuente_texto, width=10, bd=1, relief="solid")
entry_nota2.grid(row=2, column=1, sticky="w", padx=10, pady=5)

btn_agregar = tk.Button(
    frame_form,
    text="➕ Agregar Alumno",
    command=agregar_alumno,
    bg=color_primario,
    fg="white",
    font=fuente_texto,
    activebackground="#3452c2",
    relief="flat",
    padx=10,
    pady=5
)
btn_agregar.grid(row=3, column=0, columnspan=2, pady=15)

# Tabla
estilo = ttk.Style()
estilo.theme_use("default")
estilo.configure("Treeview.Heading", font=("Helvetica", 11, "bold"), background="#f5f5f5", foreground="black")
estilo.configure("Treeview", font=fuente_texto, rowheight=30, fieldbackground=color_fondo, background=color_fondo)

tabla = ttk.Treeview(root, columns=("Nombre", "Nota 1", "Nota 2", "Promedio"), show="headings")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Nota 1", text="Nota 1")
tabla.heading("Nota 2", text="Nota 2")
tabla.heading("Promedio", text="Promedio")
tabla.pack(pady=20, fill="x", padx=30)

# Búsqueda
frame_busqueda = tk.Frame(root, bg=color_fondo)
frame_busqueda.pack(pady=10)

tk.Label(frame_busqueda, text="🔍 Buscar alumno:", font=fuente_texto, bg=color_fondo).pack(side="left", padx=5)
entry_busqueda = tk.Entry(frame_busqueda, font=fuente_texto, width=25, bd=1, relief="solid")
entry_busqueda.pack(side="left", padx=5)

btn_buscar = tk.Button(
    frame_busqueda,
    text="Buscar Promedio",
    command=buscar_promedio,
    bg="black",
    fg="white",
    font=fuente_texto,
    activebackground="#333333",
    relief="flat",
    padx=10,
    pady=5
)
btn_buscar.pack(side="left", padx=5)

root.mainloop()
