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

        # Cargar imágenes
        self.img_bandera = PhotoImage(file="Bandera.png")
        self.img_explosion = PhotoImage(file="Explosion.png")
        self.img_mina = PhotoImage(file="Mina.png")

        self.crear_tablero()
        self.colocar_minas()
        self.calcular_adyacentes()

    def crear_tablero(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                boton = tk.Button(
                    self.root,
                    text='',
                    borderwidth=1,  # Opcional: para que se vea más prolijo
                    relief='raised'
                )
                boton.config(command=lambda x=i, y=j: self.descubrir_casilla(x, y))
                boton.bind('<Button-3>', lambda event, x=i, y=j: self.marcar_casilla(event, x, y))
                boton.grid(row=i, column=j)
                self.botones[i][j] = boton

    def marcar_casilla(self, event, fila, columna):
        if self.juego_terminado:
            return
        boton = self.botones[fila][columna]
        if boton['text'] == '' and not boton['image']:
            boton.config(image=self.img_bandera, text='')
            boton['state'] = 'disabled'
            boton['bg'] = 'yellow'
        elif boton['image']:
            boton.config(image='', text='')
            boton['state'] = 'normal'
            boton['bg'] = 'SystemButtonFace'

    def revelar_minas(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                boton = self.botones[i][j]
                if self.tablero[i][j] == -1:
                    boton.config(image=self.img_mina, text='')
                    boton['state'] = 'disabled'
                    boton['bg'] = 'red'
                else:
                    boton['state'] = 'disabled'
                    boton['bg'] = 'SystemButtonFace'

    def descubrir_casilla(self, fila, columna):
        if self.juego_terminado:
            return
        if self.tablero[fila][columna] == -1:
            self.botones[fila][columna].config(image=self.img_explosion, text='')
            messagebox.showinfo("Fin del juego", "¡Perdiste!")
            self.juego_terminado = True
            self.revelar_minas()
        else:
            self.revelar_casilla(fila, columna)

    def revelar_casilla(self, fila, columna):
        if self.botones[fila][columna]['state'] == 'disabled':
            return
        if self.tablero[fila][columna] == 0:
            self.botones[fila][columna].config(text='', image='')
        else:
            self.botones[fila][columna].config(text=str(self.tablero[fila][columna]), image='')
        self.botones[fila][columna]['state'] = 'disabled'
        if self.tablero[fila][columna] == 0:
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
