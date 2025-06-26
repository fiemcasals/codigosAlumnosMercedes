import random

class Buscaminas:
    def __init__(self, filas, columnas, cantidad_minas):
        self.filas =filas
        self.columnas = columnas
        self.cantidad_minas = cantidad_minas
        self.tablero = [['0' for _ in range(columnas)] for _ in range(filas)]
        self.visible = [['#' for _ in range(columnas)] for _ in range(filas)]
        self.minas = set ()  # conjunto para evitar minas duplicadas
        self.generar_minas()
        self.calcular_numeros()

    def generar_minas(self):
        while len(self.minas) < self.cantidad_minas:
            fila = random.randint(0, self.filas -1)
            columna = random.randint (0, self.columnas -1)
            self.minas.add((fila, columna)) #el conjunto con el metodo add los ingresa de manera ordenada y sin duplicados
        for f, c in self.minas:
            self.tablero[f][c] = '*'

    def calcular_numeros(self):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if self.tablero[fila][columna] == '*':
                    continue
                minas_cerca = 0
                for i in range(- 1, 2):
                    for j in range(- 1, 2):
                        nf, nc = fila + i, columna + j
                        if 0 <= nf < self.filas and 0 <= nc < self.columnas: #condicional que verifica que no salga del tablero desde el numero de fila y columna
                            if self.tablero[nf][nc] == '*':
                                minas_cerca += 1
                self.tablero[fila][columna] = str(minas_cerca) 

    def mostrar_tablero(self):
        print("\nTablero:")
        print("\n   ", end="")  # espacio para alinear con los índices de fila
        for col in range(self.columnas):
            print(f"{col:2} ", end="") # imprime indices de las columna
        print() # salto de linea
        print("   " + "---" * self.columnas)
        
        for i, fila in enumerate(self.visible):
            print(f"{i:2}|", end=" ")  # imprime el indice y la separacio " | " de la fila
            for celda in fila:
                print(f"{celda:2}", end=" ") # imprime cada celda de la fila
            print() # salto de linea al final de cada fila

    def descubrir(self, fila, columna):
        if not (0 <= fila < self.filas and 0 <= columna < self.columnas):
            print(f"Coordenadas fuera del tablero.")
            return False
        
        if self.visible[fila][columna] != '#':
            print(f"Esta celda ya fue descubierta.")
            return False
        
        if self.tablero[fila][columna] == '*':
            self.visible[fila][columna] = '*'
            return True
        
        self.revelar_celda(fila, columna)
        return True
    
    def revelar_celda(self, fila, columna):
        if not (0<= fila < self.filas and 0 <= columna < self.columnas):
            return
        if self.visible[fila][columna] != '#':
            return
        self.visible[fila][columna] = self.tablero[fila][columna]

        if self.tablero[fila][columna] == '0':
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    self.revelar_celda(fila + i, columna + j)

    def juego_terminado(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                if self.visible[f][c] == '#' and self.tablero[f][c] != '*':
                    return False
        return True
    
def jugar():
    print(f"Bienvenido al Buscaminas en Python 🧨\n")

    filas = int(input("👉Ingresa cantidad de filas: ") or 8)
    columnas = int(input("👉Ingresa cantidad de columnas: ") or 8)
    minas = int(input("💣Ingresa cantidad de minas: ") or 10)

    try:
        vidas = int(input("👉Ingresa cantidad de vidas: ") or 3)
    except ValueError:
        print(f"⚠️ Dato invalido. Ingresa solo numeros.")
        return

    juego = Buscaminas(filas, columnas, minas)

    while True:
        juego.mostrar_tablero()
        print(f"💖 Quedan: {vidas} vidas.")

        accion = input("¿Querés descubrir (D) o marcar/desmarcar (M)? ").lower()
        if accion not in ['d', 'm']:
            print("⚠️ Acción no válida. Usá 'D' para descubrir o 'M' para marcar.")
            continue

        try:
            f = int(input("Ingrese la fila: "))
            c = int(input("Ingrese la columna: "))
        except ValueError:
            print(f"⚠️ Dato invalido. Ingresa solo numeros.")
            continue

        if not (0 <= f < filas and 0 <= c < columnas):
            print("⚠️ Coordenadas fuera del tablero.")
            continue

        if accion == 'm':
            if juego.visible[f][c] == '#':
                juego.visible[f][c] = '🚩'
            elif juego.visible[f][c] == '🚩':
                juego.visible[f][c] = '#'
            else:
                print("⚠️ Esta celda ya fue descubierta, no se puede marcar.")
            continue  # volvemos al loop sin descubrir

        resultado = juego.descubrir(f, c)

        if not resultado:
            continue

        if juego.tablero[f][c] == '*':
            vidas -= 1
            print(f"💥 ¡Pisaste una mina!")
            if vidas <= 0:
                print(f"💀 Te quedaste sin vidas. Fin del juego")
                # Revelar todas las minas al perder
                for fila in range(juego.filas):
                    for columna in range(juego.columnas):
                        if juego.tablero[fila][columna] == 'O':
                            juego.visible[fila][columna] = '💣'
                juego.mostrar_tablero()
                break  # ✅ ESTE break debe estar DENTRO del if
            continue  # ✅ Si te quedan vidas, sigue el juego


        if juego.juego_terminado():
            juego.mostrar_tablero()
            print(f"🎉 ¡FELICITACIONES! Ganaste el juego.")
            break


if __name__ == "__main__":
    while True:
        jugar()
        respuesta = input("\n¿Volver a jugar? (S/N): ").lower()
        if respuesta != 's':
            print(f"¡Gracias por jugar! 👋")
            break
