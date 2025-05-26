import random

# Crear un tablero vacío
def crear_tablero():
    return [["_" for _ in range(5)] for _ in range(5)]

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

# Colocar minas aleatoriamente
def colocar_minas(tablero, num_minas):
    minas_colocadas = 0
    while minas_colocadas < num_minas:
        fila = random.randint(0, 4)
        columna = random.randint(0, 4)
        if tablero[fila][columna] == "_":
            tablero[fila][columna] = "*"
            minas_colocadas += 1

# Realizar una busqueda de mina en el tablero (aca tengo que modificar el codigo para que busque minas)
def busca_mina(tablero, fila, columna):
    if tablero[fila][columna] == "*":
        tablero[fila][columna] = "X"
        return True
    elif tablero[fila][columna] == "~":
        tablero[fila][columna] = "O"
        return False
    return None

# Comprobar si quedan minas
def quedan_minas(tablero):
    for fila in tablero:
        if "*" in fila:
            return True
    return False

# Juego principal
def busca_minasl():
    print("¡Buscaminas!")
    tablero_jugador = crear_tablero()

    # Colocar barcos (5 barcos para cada jugador)
    colocar_minas(tablero_jugador, 5)

    while True:
        print("\nTu tablero:")
        mostrar_tablero(tablero_jugador)
    

        # Turno del jugador
        print("\nTu turno:")
        try:
            fila = input("Ingresa la fila (1-5): ")
            columna = input("Ingresa la columna (A-E): ")
            if not fila.isdigit() or int(fila) < 1 or int(fila) > 5 or columna.upper() not in "ABCDE":
                print("Coordenadas fuera de rango. Intentá de nuevo.")
                continue
            fila_idx, columna_idx = convertir_coordenadas(fila, columna)
            resultado = atacar(tablero_computadora, fila_idx, columna_idx)
            if resultado is True:
                print("¡Pisaste una mina!")
            elif resultado is False:
                print("Agua.")
            else:
                print("Ya pisaste esa posición.")
        except ValueError:
            print("Entrada inválida. Intentá de nuevo.")
            continue

        # Comprobar si el jugador ganó
        if not quedan_minas(tablero_jugador):
            print("¡Felicitaciones! ¡Encontraste todas las minas! Fin del juego.")
            break

# Ejecutar el juego
if __name__ == "__main__":
    busca_minas()