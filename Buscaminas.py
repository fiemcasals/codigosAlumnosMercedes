import random

# Crear un tablero vacío
def crear_tablero():
    return [["_" for _ in range(5)] for _ in range(5)]

# Mostrar el tablero visible para el jugador
def mostrar_tablero(tablero_visible):
    columnas = "A B C D E".split()
    print("  " + " ".join(columnas))
    for idx, fila in enumerate(tablero_visible, start=1):
        print(f"{idx:2} " + " ".join(fila))

# Convertir coordenadas de entrada (ej. 1A) a índices
def convertir_coordenadas(fila, columna):
    fila_idx = int(fila) - 1
    columna_idx = ord(columna.upper()) - ord('A')
    return fila_idx, columna_idx

# Colocar minas aleatoriamente
def colocar_minas(tablero, num_minas):
    minas_colocadas = 0
    while minas_colocadas < num_minas:
        fila = random.randint(0, 4)
        columna = random.randint(0, 4)
        if tablero[fila][columna] == "_":
            tablero[fila][columna] = "*"
            minas_colocadas += 1

# Contar minas alrededor de una casilla
def contar_minas_alrededor(tablero, fila, columna):
    minas = 0
    for i in range(fila-1, fila+2):
        for j in range(columna-1, columna+2):
            if 0 <= i < 5 and 0 <= j < 5 and not (i == fila and j == columna):
                if tablero[i][j] == "*":
                    minas += 1
    return minas

# Descubrir casilla (y recursivamente si no hay minas alrededor)
def descubrir(tablero, visible, fila, columna):
    if visible[fila][columna] != "_":
        return
    if tablero[fila][columna] == "*":
        visible[fila][columna] = "*"
        return
    minas = contar_minas_alrededor(tablero, fila, columna)
    visible[fila][columna] = str(minas)
    if minas == 0:
        visible[fila][columna] = " "
        for i in range(fila-1, fila+2):
            for j in range(columna-1, columna+2):
                if 0 <= i < 5 and 0 <= j < 5:
                    descubrir(tablero, visible, i, j)

# Comprobar si el jugador ha ganado
def ha_ganado(tablero, visible):
    for i in range(5):
        for j in range(5):
            if tablero[i][j] != "*" and visible[i][j] == "_":
                return False
    return True

# Juego principal
def buscaminas():
    print("¡Buscaminas!")
    tablero = crear_tablero()
    visible = crear_tablero()
    colocar_minas(tablero, 5)

    while True:
        print("\nTablero:")
        mostrar_tablero(visible)
        try:
            fila = input("Ingresa la fila (1-5): ")
            columna = input("Ingresa la columna (A-E): ")
            if not fila.isdigit() or int(fila) < 1 or int(fila) > 5 or columna.upper() not in "ABCDE":
                print("Coordenadas fuera de rango. Intentá de nuevo.")
                continue
            fila_idx, columna_idx = convertir_coordenadas(fila, columna)
            if visible[fila_idx][columna_idx] != "_":
                print("Ya descubriste esa casilla.")
                continue
            if tablero[fila_idx][columna_idx] == "*":
                # Mostrar todas las minas
                for i in range(5):
                    for j in range(5):
                        if tablero[i][j] == "*":
                            visible[i][j] = "*"
                mostrar_tablero(visible)
                print("¡Pisaste una mina! Fin del juego.")
                break
            descubrir(tablero, visible, fila_idx, columna_idx)
            if ha_ganado(tablero, visible):
                mostrar_tablero(visible)
                print("¡Felicitaciones! ¡Ganaste!")
                break
        except ValueError:
            print("Entrada inválida. Intentá de nuevo.")

if __name__ == "__main__":
    buscaminas()