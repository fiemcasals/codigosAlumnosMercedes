# Juego de buscaminas en tkinter, donde el usuario puede hacer clic en las casillas para descubrirlas. el usuario elige el tamaño del tablero y la cantidad de vidas
import tkinter as tk
import random
import tkinter.messagebox as messagebox

def crear_tablero(tamano):
    return [["_" for _ in range(tamano)] for _ in range(tamano)]
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()
def convertir_coordenadas(fila, columna):
    fila_idx = int(fila) - 1
    columna_idx = ord(columna.upper()) - ord('A')
    return fila_idx, columna_idx
def colocar_minas(tablero, num_minas):
    minas_colocadas = 0
    tamano = len(tablero)
    while minas_colocadas < num_minas:
        fila = random.randint(0, tamano - 1)
        columna = random.randint(0, tamano - 1)
        if tablero[fila][columna] == "_":
            tablero[fila][columna] = "*"
            minas_colocadas += 1
def contar_minas_alrededor(tablero, fila, columna):
    minas = 0
    tamano = len(tablero)
    for i in range(max(0, fila - 1), min(tamano, fila + 2)):
        for j in range(max(0, columna - 1), min(tamano, columna + 2)):
            if (i != fila or j != columna) and tablero[i][j] == "*":
                minas += 1
    return minas
def descubrir(tablero, visible, fila, columna):
    if visible[fila][columna] != "_":
        return
    if tablero[fila][columna] == "*":
        visible[fila][columna] = "*"
        return
    minas = contar_minas_alrededor(tablero, fila, columna)
    visible[fila][columna] = str(minas) if minas > 0 else " "
    if minas == 0:
        for i in range(max(0, fila - 1), min(len(tablero), fila + 2)):
            for j in range(max(0, columna - 1), min(len(tablero), columna + 2)):
                descubrir(tablero, visible, i, j)
def ha_ganado(tablero, visible):
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] != "*" and visible[i][j] == "_":
                return False
    return True
def clic_casilla(fila, columna):
    fila_idx, columna_idx = convertir_coordenadas(fila, columna)
    if tablero[fila_idx][columna_idx] == "*":
        visible[fila_idx][columna_idx] = "*"
        messagebox.showinfo("Fin del juego", "¡Has perdido!")
        mostrar_tablero(visible)
    else:
        descubrir(tablero, visible, fila_idx, columna_idx)
        if ha_ganado(tablero, visible):
            messagebox.showinfo("Fin del juego", "¡Has ganado!")
            mostrar_tablero(visible)
    actualizar_tablero_gui()
def actualizar_tablero_gui():
    for i in range(tamano):
        for j in range(tamano):
            if visible[i][j] == "_":
                botones[i][j].config(text="", state=tk.NORMAL)
            elif visible[i][j] == "*":
                botones[i][j].config(text="*", state=tk.DISABLED, bg="red")
            else:
                botones[i][j].config(text=visible[i][j], state=tk.DISABLED)
def iniciar_juego():
    global tablero, visible, botones, tamano
    tamano = int(entry_tamano.get())
    num_minas = int(entry_minas.get())
    tablero = crear_tablero(tamano)
    visible = crear_tablero(tamano)
    colocar_minas(tablero, num_minas)
    
    for i in range(tamano):
        for j in range(tamano):
            botones[i][j].config(text="_", state=tk.NORMAL, bg="SystemButtonFace")
    
    actualizar_tablero_gui()
# Configuración de la ventana principal
root = tk.Tk()
root.title("Buscaminas")
root.geometry("400x400")
# Entradas para el tamaño del tablero y número de minas
label_tamano = tk.Label(root, text="Tamaño del tablero (NxN):")
label_tamano.pack()
entry_tamano = tk.Entry(root)
entry_tamano.pack()
label_minas = tk.Label(root, text="Número de minas:")
label_minas.pack()
entry_minas = tk.Entry(root)
entry_minas.pack()
# Botón para iniciar el juego
button_iniciar = tk.Button(root, text="Iniciar Juego", command=iniciar_juego)
button_iniciar.pack()
# Crear botones para el tablero
tamano = 5  # Tamaño por defecto del tablero
botones = []
for i in range(tamano):
    fila_botones = []
    for j in range(tamano):
        boton = tk.Button(root, text="_", width=3, height=1,
                          command=lambda fila=i+1, columna=chr(j + ord('A')): clic_casilla(fila, columna))
        boton.grid(row=i, column=j)
        fila_botones.append(boton)
    botones.append(fila_botones)
# Inicializar el tablero y la visibilidad
tablero = crear_tablero(tamano)
visible = crear_tablero(tamano)
# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
# Mostrar el tablero inicial
mostrar_tablero(tablero)
# Mostrar el tablero visib le inicial
mostrar_tablero(visible)
# Mostrar el tablero inicial
# mostrar_tablero(visible)
# Mostrar el tablero visible inicial