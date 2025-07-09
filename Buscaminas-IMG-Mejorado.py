# Juego de buscaminas en tkinter, donde el usuario puede hacer clic en las casillas para descubrirlas. con el boton derecho se marca la casilla que coniene una mina y con el izquierdo se descubre la casilla.
import random
import tkinter.messagebox as messagebox
import tkinter as tk
from tkinter import PhotoImage

class Buscaminas:
    def __init__(self, root, filas=10, columnas=10, minas=10):
        self.root = root
        self.filas = filas
        self.columnas = columnas
        self.minas = minas
        self.tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
        self.botones = [[None for _ in range(columnas)] for _ in range(filas)]
        self.minas_colocadas = 0
        self.juego_terminado = False
        self.minas_marcadas = 0
        self.tiempo = 0
        self.temporizador_iniciado = False
        self.temporizador_id = None

        # Contadores
        self.frame_superior = tk.Frame(self.root)
        self.frame_superior.grid(row=0, column=0, columnspan=columnas)
        self.label_tiempo = tk.Label(self.frame_superior, text="Tiempo: 0s", font=("Arial", 12))
        self.label_tiempo.pack(side=tk.LEFT, padx=10)
        self.label_minas = tk.Label(self.frame_superior, text=f"Minas marcadas: 0/{self.minas}", font=("Arial", 12))
        self.label_minas.pack(side=tk.LEFT, padx=10)

        # Cargar imágenes
        self.img_bandera = PhotoImage(file="Casilla_banderin.png")
        self.img_explosion = PhotoImage(file="Explosion.png")
        self.img_mina = PhotoImage(file="Casilla_mina.png")
        self.img_sin_descubrir = PhotoImage(file="Casilla_sin_descubrir.png")
        self.img_descubierta = PhotoImage(file="Casilla_descubierta.png")
        self.img_numeros = [None] + [PhotoImage(file=f"Casilla_{i}.png") for i in range(1,9)]
        # img_numeros[1] = Casilla_1.png, ..., img_numeros[8] = Casilla_8.png

        self.crear_tablero()
        self.colocar_minas()
        self.calcular_adyacentes()

    def iniciar_temporizador(self):
        if not self.temporizador_iniciado:
            self.temporizador_iniciado = True
            self.actualizar_tiempo()

    def actualizar_tiempo(self):
        if not self.juego_terminado:
            self.tiempo += 1
            self.label_tiempo.config(text=f"Tiempo: {self.tiempo}s")
            self.temporizador_id = self.root.after(1000, self.actualizar_tiempo)

    def crear_tablero(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                boton = tk.Button(
                    self.root,
                    image=self.img_sin_descubrir,  # Imagen de casilla sin descubrir
                    borderwidth=1,
                    relief='raised',
                    width=32,  # Ajusta el tamaño según tus imágenes
                    height=32
                )
                boton.config(command=lambda x=i, y=j: self.descubrir_casilla(x, y))
                boton.bind('<Button-3>', lambda event, x=i, y=j: self.marcar_casilla(event, x, y))
                boton.grid(row=i+1, column=j)  # +1 para dejar espacio al frame superior
                self.botones[i][j] = boton

    def marcar_casilla(self, event, fila, columna):
        if self.juego_terminado:
            return
        boton = self.botones[fila][columna]
        if boton['state'] == 'normal' and boton['image'] == str(self.img_sin_descubrir):
            boton.config(image=self.img_bandera)
            self.minas_marcadas += 1
        elif boton['image'] == str(self.img_bandera):
            boton.config(image=self.img_sin_descubrir)
            self.minas_marcadas -= 1
        self.label_minas.config(text=f"Minas marcadas: {self.minas_marcadas}/{self.minas}")

    def revelar_minas(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                boton = self.botones[i][j]
                if self.tablero[i][j] == -1:
                    boton.config(image=self.img_mina)
                boton['state'] = 'disabled'

    def descubrir_casilla(self, fila, columna):
        if self.juego_terminado:
            return
        self.iniciar_temporizador()
        if self.tablero[fila][columna] == -1:
            self.botones[fila][columna].config(image=self.img_explosion)
            messagebox.showinfo("Fin del juego", "¡Perdiste!")
            self.juego_terminado = True
            if self.temporizador_id:
                self.root.after_cancel(self.temporizador_id)
            self.revelar_minas()
        else:
            self.revelar_casilla(fila, columna)

    def revelar_casilla(self, fila, columna):
        if self.botones[fila][columna]['state'] == 'disabled':
            return
        valor = self.tablero[fila][columna]
        if valor == 0:
            self.botones[fila][columna].config(image=self.img_descubierta)
        else:
            self.botones[fila][columna].config(image=self.img_numeros[valor])
        self.botones[fila][columna]['state'] = 'disabled'
        if valor == 0:
            for x in range(max(0, fila - 1), min(self.filas, fila + 2)):
                for y in range(max(0, columna - 1), min(self.columnas, columna + 2)):
                    if (x != fila or y != columna) and self.botones[x][y]['state'] != 'disabled':
                        self.revelar_casilla(x, y)

    def colocar_minas(self):
        while self.minas_colocadas < self.minas:
            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)
            if self.tablero[fila][columna] != -1:
                self.tablero[fila][columna] = -1
                self.minas_colocadas += 1

    def calcular_adyacentes(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.tablero[i][j] == -1:
                    continue
                minas_adyacentes = 0
                for x in range(max(0, i - 1), min(self.filas, i + 2)):
                    for y in range(max(0, j - 1), min(self.columnas, j + 2)):
                        if self.tablero[x][y] == -1:
                            minas_adyacentes += 1
                self.tablero[i][j] = minas_adyacentes

def main():
    root = tk.Tk()
    root.title("Buscaminas")
    buscaminas = Buscaminas(root, filas=10, columnas=10, minas=10)
    root.mainloop()
if __name__ == "__main__":
    main()
