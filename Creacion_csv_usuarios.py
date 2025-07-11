# Codigo implementado en tkinter para crear archivo .csv con los datos que se cargan desde teclado. Se pide cargar nombre, apellido y edad, el nombre y el contenido del archivo son los datos cargados, separados por comas. El archivo debe llamarse "alumnos.csv". Debe funcionar hasta que se presione el boton "Salir". El archivo, si no existe, se debe crear en la carpeta "alumnos" y si existe los datos se deben agregar. El archivo debe tener el encabezado "Nombre,Apellido,Edad"
import tkinter as tk
from tkinter import messagebox
import csv
import os

class AppAlumnos:
    def __init__(self, master):
        self.master = master
        master.title("Carga de alumnos")
        master.geometry("350x220")

        tk.Label(master, text="Nombre:").pack(pady=(10,0))
        self.entry_nombre = tk.Entry(master)
        self.entry_nombre.pack()

        tk.Label(master, text="Apellido:").pack(pady=(10,0))
        self.entry_apellido = tk.Entry(master)
        self.entry_apellido.pack()

        tk.Label(master, text="Edad:").pack(pady=(10,0))
        self.entry_edad = tk.Entry(master)
        self.entry_edad.pack()

        tk.Button(master, text="Guardar", command=self.guardar_datos).pack(pady=(15,5))
        tk.Button(master, text="Salir", command=self.salir).pack(pady=(0,10))

    def guardar_datos(self):
        nombre = self.entry_nombre.get().strip()
        apellido = self.entry_apellido.get().strip()
        edad = self.entry_edad.get().strip()
        if not nombre or not apellido or not edad:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        if not edad.isdigit():
            messagebox.showerror("Error", "La edad debe ser un número.")
            return

        # Verificar si la carpeta "alumnos" existe, si no, crearla
        if not os.path.exists("alumnos"):
            os.makedirs("alumnos")
        archivo_csv = os.path.join("alumnos", "alumnos.csv")
        file_exists = os.path.isfile(archivo_csv)

        with open(archivo_csv, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Nombre", "Apellido", "Edad"])
            writer.writerow([nombre, apellido, edad])
        messagebox.showinfo("Guardado", f"Datos de {nombre} {apellido} guardados correctamente.")
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellido.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)

    def salir(self):
        self.master.destroy()
        messagebox.showinfo("Proceso terminado", "Los datos se han guardado en 'alumnos/alumnos.csv'.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppAlumnos(root)
    root.mainloop()
