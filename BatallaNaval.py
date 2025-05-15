import random

# Crear un tablero vacío
def crear_tablero():
    return [["~" for _ in range(5)] for _ in range(5)]

# Mostrar el tablero
def mostrar_tablero(tablero):
    columnas = "A B C D E".split()
    print("  " + " ".join(columnas))
    for idx, fila in enumerate(tablero, start=1):
        print(f"{idx:2} " + " ".join(fila))

# Convertir coordenadas de entrada (ej. 1A) a índices
def convertir_coordenadas(fila, columna):
    fila_idx = int(fila) - 1
    columna_idx = ord(columna.upper()) - ord('A')
    return fila_idx, columna_idx

# Colocar barcos aleatoriamente
def colocar_barcos(tablero, num_barcos):
    barcos_colocados = 0
    while barcos_colocados < num_barcos:
        fila = random.randint(0, 4)
        columna = random.randint(0, 4)
        if tablero[fila][columna] == "~":
            tablero[fila][columna] = "B"
            barcos_colocados += 1

# Realizar un ataque
def atacar(tablero, fila, columna):
    if tablero[fila][columna] == "B":
        tablero[fila][columna] = "X"
        return True
    elif tablero[fila][columna] == "~":
        tablero[fila][columna] = "O"
        return False
    return None

# Comprobar si quedan barcos
def quedan_barcos(tablero):
    for fila in tablero:
        if "B" in fila:
            return True
    return False

# Juego principal
def batalla_naval():
    print("¡Batalla Naval!")
    tablero_jugador = crear_tablero()
    tablero_computadora = crear_tablero()

    # Colocar barcos (5 barcos para cada jugador)
    colocar_barcos(tablero_computadora, 5)
    colocar_barcos(tablero_jugador, 5)

    while True:
        print("\nTu tablero:")
        mostrar_tablero(tablero_jugador)
        print("\nTablero de la computadora:")
        mostrar_tablero([["~" if celda == "B" else celda for celda in fila] for fila in tablero_computadora])

        # Turno del jugador
        print("\nTu turno:")
        try:
            fila = input("Ingresa la fila (1-5): ")
            columna = input("Ingresa la columna (A-E): ")
            if not fila.isdigit() or int(fila) < 1 or int(fila) > 5 or columna.upper() not in "ABCDE":
                print("Coordenadas fuera de rango. Intenta de nuevo.")
                continue
            fila_idx, columna_idx = convertir_coordenadas(fila, columna)
            resultado = atacar(tablero_computadora, fila_idx, columna_idx)
            if resultado is True:
                print("¡Hundido!")
            elif resultado is False:
                print("Agua.")
            else:
                print("Ya atacaste esa posición.")
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")
            continue

        # Comprobar si el jugador ganó
        if not quedan_barcos(tablero_computadora):
            print("¡Felicidades! Hundiste todos los barcos de la computadora.")
            break

        # Turno de la computadora
        print("\nTurno de la computadora:")
        while True:
            fila = random.randint(0, 4)
            columna = random.randint(0, 4)
            if tablero_jugador[fila][columna] in ["~", "B"]:
                break
        resultado = atacar(tablero_jugador, fila, columna)
        if resultado is True:
            print(f"La computadora atacó ({fila + 1}, {chr(columna + ord('A'))}) y acertó.")
        elif resultado is False:
            print(f"La computadora atacó ({fila + 1}, {chr(columna + ord('A'))}) y falló.")

        # Comprobar si la computadora ganó
        if not quedan_barcos(tablero_jugador):
            print("¡La computadora hundió todos tus barcos! Fin del juego.")
            break

# Ejecutar el juego
if __name__ == "__main__":
    batalla_naval()