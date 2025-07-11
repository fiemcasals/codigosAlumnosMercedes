# Codigo implementado en tkinter para crear archivos de texto con los datos que se cargan desde teclado. Se pide cargar nombre, apellido y edad, el nombre del archivo se crea a partir de la concatenacion del nombre_apellido.csv y el contenido del archivo son los datos cargados, separados por comas. Debe funcionar hasta que se presione el boton "salir". los archivos se deben crear en la carpeta "usuarios".

import os
import csv
import tkinter as tk
from tkinter import messagebox
class CreacionArchivos:
    def __init__(self, master):
        self.master = master
        self.master.title("Creación de Archivos")
        self.master.geometry("300x300")

        # Crear carpeta "usuarios" si no existe
        if not os.path.exists("usuarios"):
            os.makedirs("usuarios")

        # Etiquetas y campos de entrada
        tk.Label(master, text="Nombre:").pack(pady=5)
        self.nombre_entry = tk.Entry(master)
        self.nombre_entry.pack(pady=5)

        tk.Label(master, text="Apellido:").pack(pady=5)
        self.apellido_entry = tk.Entry(master)
        self.apellido_entry.pack(pady=5)

        tk.Label(master, text="Edad:").pack(pady=5)
        self.edad_entry = tk.Entry(master)
        self.edad_entry.pack(pady=5)

        # Botones
        tk.Button(master, text="Guardar", command=self.guardar_datos).pack(pady=5)
        tk.Button(master, text="Salir", command=master.quit).pack(pady=5)

    def guardar_datos(self):
        nombre = self.nombre_entry.get().strip()
        apellido = self.apellido_entry.get().strip()
        edad = self.edad_entry.get().strip()

        if not nombre or not apellido or not edad:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        # Crear el nombre del archivo
        filename = f"usuarios/{nombre}_{apellido}.csv"

        # Guardar los datos en el archivo CSV
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nombre, apellido, edad])

        messagebox.showinfo("Éxito", f"Datos guardados en {filename}")
        
        # Limpiar los campos de entrada
        self.nombre_entry.delete(0, tk.END)
        self.apellido_entry.delete(0, tk.END)
        self.edad_entry.delete(0, tk.END)
def main():
    root = tk.Tk()
    app = CreacionArchivos(root)
    root.mainloop()
if __name__ == "__main__":
    main()

