"""
Batalla naval
agua              = ~
disparo al agua   = x
jugador 1         = 1
jugador 1 hundido = %
jugador 2         = 2
jugador 2 hundido = *

La logica de dividir el tablero solo sirve para este de 5x5
ya que agarra las pimeras 2 filas para el que ataca y las ultimas 2 para el oponente
seria mejor calcular la linea del centro, y dar a cada jugador la parte de arriba y abajo
asi funcionaria para cualquier tablero N impar

"""
import numpy as np
from pandas import DataFrame


def crear_tablero(filas, cols, agua="~"):
    return np.full((filas, cols), fill_value=agua)

def colocar_naves(tablero, cant_naves, jugador, agua="~"):
    if jugador == 1:
        tablero_jugador = tablero[:2, :]  # primeras 2 filas
    elif jugador == 2:
        tablero_jugador = tablero[-2:, :]  # ultimas 2 filas
    else:
        print(f"Numero de jugador invalido: {jugador}\nTiene que ser ( 1 o 2 )")
        return

    print("-" * 30)
    print(f"Poniendo naves para jugador: {jugador}")
    print("-" * 30)

    nave = jugador
    naves_puestas = 0

    while naves_puestas < cant_naves:
        # filas de la porcion del tablero que le pertenece al jugador en cuestion
        filas_disponibles = tablero_jugador.shape[0]
        random_row = np.random.randint(0, filas_disponibles)

        random_key = np.random.choice(list(columnas.keys()))
        random_col = columnas[random_key]

        posicion = tablero_jugador[random_row, random_col]

        if posicion == agua:  # si no hay una nave en esa posicion
            # esto se castea como string cuando el agua no es 0
            tablero_jugador[random_row, random_col] = nave
            print(f"Coordenada: [{random_row},{random_col}], Valor: {agua}")

            naves_puestas += 1
            print(f"+1 nave en posicion [{random_key},{random_row}]\n")
        else:
            print(f"Ya hay una nave en posicion [{random_key},{random_row}]\n")

    print(f"Naves agregadas: {naves_puestas}\n")


def mostrar_tablero(tablero) -> DataFrame:
    return DataFrame(tablero, columns=columnas.keys())


def disparar(tablero, coordenadas: tuple[str, int], atacante, agua="~"):
    # invertido a la funcion colocar_naves ya que disparas al enemigo
    if atacante == 1:
        tablero_jugador = tablero[-2:, :]  # ultimas 2 filas
        hundido = "*"
        oponente = str(2)
    elif atacante == 2:
        tablero_jugador = tablero[:2, :]  # primeras 2 filas
        hundido = "%"
        oponente = str(1)
    else:
        print(f"Numero de jugador invalido: {atacante}\nTiene que ser ( 1 o 2 )")
        return 0

    nave = oponente
    fila = coordenadas[1]
    columna = columnas[coordenadas[0]]
    print(f"fila: {fila}, columna: {columna}")
    posicion = tablero_jugador[fila, columna]

    if posicion == agua or posicion == "x":
        tablero_jugador[fila, columna] = "x"
    elif posicion == hundido:
        pass
    elif posicion == nave:
        tablero_jugador[fila, columna] = hundido
        return 1


def main():
    global columnas
    columnas = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
    filas, cols = (5, 5)
    # checkear que cantidad de naves no exceda (filas del jugador * n_cols)

    agua = "~"

    # iniciar tablero en '~' u otro caracter
    tablero = crear_tablero(filas, cols)

    empieza = np.random.randint(1, 3)
    atacante = empieza
    # asignar numero contrario al que empezo
    oponente = 2 if (empieza == 1) else 1

    cant_naves_atacante = 3
    cant_naves_oponente = 3
    
    colocar_naves(tablero, cant_naves_atacante, atacante)
    colocar_naves(tablero, cant_naves_oponente, oponente)

    jugador_input = " "

    print("-" * 20)
    print(" <<[Batalla naval]>>")
    print("-" * 20)

    print(f"Empieza atacando el jugador {empieza}\n")
    turno = 1

    # mostrar tablero
    df = mostrar_tablero(tablero)
    print(df, "\n")
    
    while jugador_input != "q":

        print(f"Cantidad de naves del atacante: {cant_naves_atacante}")
        print(f"Cantidad de naves del oponente: {cant_naves_oponente}\n")

        print(f"Atacante actual: jugador {atacante}")
        print(f"Turno actual: {turno}")
        turno += 1

        jugador_input = input('\nIngresa una posicion: ( [A-E], [0-1] ) o "q" para salir: ')
        if jugador_input.lower() == "q":
            print("\nNos vimos"); break

        if jugador_input.lower() == "bomba nuclear":
            tablero[:, :] = "@"
            df = mostrar_tablero(tablero)
            # df.style.set_properties(**{'font-size': '25px'})    ## solo para el notebook
            print(df, "\n")
            print("Kaboom!")
            break

        fila = jugador_input[0].upper()
        columna = int(jugador_input[1])
        coordenadas = (fila, columna)
        
        # pium
        catapum = disparar(tablero, coordenadas, atacante)
        if catapum:
            if atacante == empieza:
                cant_naves_oponente -= 1
            else:
                cant_naves_atacante -= 1

        df = mostrar_tablero(tablero)
        # df.style.set_properties(**{'font-size': '25px'})    ## solo para el notebook
        print(df, "\n")
        
        # si alguien se queda sin naves, a dormir
        if cant_naves_oponente == 0 or cant_naves_atacante == 0:
            print(f"Termino el juego maestro, gano el jugador {atacante}")
            break

        # cambiar quien ataca basado en si el turno es impar o par (porque empieza en 1)
        atacante = empieza if (turno % 2 != 0) else oponente
        # print(f"Atacante luego de disparar: {atacante}")

if __name__ == "__main__":
    main()
