import random

BOARD_SIZE = 10
NUM_SHIPS = 3

def crear_tablero():
    return [["~"] * BOARD_SIZE for _ in range(BOARD_SIZE)]

def colocar_barcos(tablero):
    barcos = 0
    while barcos < NUM_SHIPS:
        fila = random.randint(0, BOARD_SIZE - 1)
        col = random.randint(0, BOARD_SIZE - 1)
        if tablero[fila][col] == "~":
            tablero[fila][col] = "B"
            barcos += 1

def mostrar_tablero(tablero, ocultar_barcos=True):
    print("  " + " ".join(str(i) for i in range(BOARD_SIZE)))
    for idx, fila in enumerate(tablero):
        if ocultar_barcos:
            print(idx, " ".join("~" if c == "B" else c for c in fila))
        else:
            print(idx, " ".join(fila))

def disparar(tablero, fila, col):
    if tablero[fila][col] == "B":
        tablero[fila][col] = "X"
        return True
    elif tablero[fila][col] == "~":
        tablero[fila][col] = "O"
        return False
    return False

def barcos_restantes(tablero):
    return sum(fila.count("B") for fila in tablero)


tablero_jugador = crear_tablero()
tablero_cpu = crear_tablero()
colocar_barcos(tablero_jugador)
colocar_barcos(tablero_cpu)

turno = 0
while barcos_restantes(tablero_jugador) > 0 and barcos_restantes(tablero_cpu) > 0:
    print("\nTu tablero:")
    mostrar_tablero(tablero_jugador, ocultar_barcos=False)
    print("\nTablero enemigo:")
    mostrar_tablero(tablero_cpu, ocultar_barcos=True)

    if turno % 2 == 0:
        print("\nTu turno:")
        try:
            fila = int(input("Fila: "))
            col = int(input("Columna: "))
        except ValueError:
            print("Entrada inválida.")
            continue
        if 0 <= fila < BOARD_SIZE and 0 <= col < BOARD_SIZE:
            if tablero_cpu[fila][col] in ["X", "O"]:
                print("Ya disparaste ahí.")
            elif disparar(tablero_cpu, fila, col):
                print("¡Tocado!")
            else:
                print("Agua.")
            turno += 1
        else:
            print("Coordenadas fuera de rango.")
    else:
        print("\nTurno de la CPU:")
        while True:
            fila = random.randint(0, BOARD_SIZE - 1)
            col = random.randint(0, BOARD_SIZE - 1)
            if tablero_jugador[fila][col] not in ["X", "O"]:
                break
        if disparar(tablero_jugador, fila, col):
            print(f"La CPU disparó a ({fila}, {col}) y te dio un barco.")
        else:
            print(f"La CPU disparó a ({fila}, {col}) y falló.")
        turno += 1

if barcos_restantes(tablero_jugador) == 0:
    print("\n¡La CPU ganó!")
else:
    print("\n¡Ganaste tú!")
