#variables
#funciones
#crear tablero / mapa ---> diccionario
#asignamos posicion de las naves / aleatorio
#mostrar tablero

#menu 
# ver su tableros / ver sus tiros / tirar / salir
#que quiere hacer ? ver el mapa de mis naves o ver los tiros

#preparacion crear tablero mio / enemigo mio de los tiros y del enemigo de los tiros
#asignamos naves a los tableros mio y de enemigos

#asignar variables filas columnas definir funciones crear un diccionario y recorrerlo con el for in range asignarle a cada fila un diccionario vacio de vuelta
#saber retornar las variables o dciionarios , colocar las naves aleatoria mente llamar a random 
#podes comparar con if elif else los valores del diccionario el diccionario se llama tablero
#sumatoria de variables naves / estructuras de repeticion hasta perder imput.upper  (transforma todo en mayuscula) lower (a minuscula)

import string
import random

# ///////Crear tablero vacío////////
def crear_tablero():
    letras = list(string.ascii_uppercase[:5]) 
    return {letra: ["~"] * 5 for letra in letras}

# ///////Mostrar tablero en consola///////
def mostrar_tablero(tablero, nombre="Jugador", ocultar=False):
    print(f"\nTablero de {nombre}")
    print("  " + " ".join([str(i+1).rjust(1) for i in range(5)])) 
    for fila in tablero:
        if ocultar:
            fila_mostrada = ["~" if celda == "O" else celda for celda in tablero[fila]]
        else:
            fila_mostrada = tablero[fila]
        print(f"{fila} " + " ".join(fila_mostrada))

#//////// Colocar barcos aleatorios//////
def colocar_barcos(tablero, cantidad=3):
    colocados = 0
    letras = list(tablero.keys())

    while colocados < cantidad:
        fila = random.choice(letras)
        col = random.randint(0, 4) 
        if tablero[fila][col] == "~":
            tablero[fila][col] = "O"
            colocados += 1

# ////////Disparar a una celda///////
def disparar(tablero, fila, col):
    if tablero[fila][col] == "O":
        tablero[fila][col] = "X"  # impacto
        return "¡Impacto!"
    elif tablero[fila][col] == "~":
        tablero[fila][col] = "*"  # agua
        return "Agua."
    else:
        return "Ya disparaste ahí."

# ///////Comprobar si quedan barcos////////
def quedan_barcos(tablero):
    for fila in tablero.values():
        if "O" in fila:
            return True
    return False

# //////Entrada del usuario////////
def entrada_valida(entrada):
    return len(entrada) == 2 and entrada[0] in string.ascii_uppercase[:5] and entrada[1] in "12345"

# //////Convertir entrada (ej. "B3") en fila y columna///////
def procesar_entrada(entrada):
    fila = entrada[0].upper()
    col = int(entrada[1]) - 1
    return fila, col

# //////Turno CPU (elige aleatoriamente)///////
def turno_cpu(tablero_jugador, tiros_cpu):
    letras = list(tablero_jugador.keys())
    while True:
        fila = random.choice(letras)
        col = random.randint(0, 4)
        if (fila, col) not in tiros_cpu:
            tiros_cpu.add((fila, col))
            resultado = disparar(tablero_jugador, fila, col)
            print(f"\nLa CPU disparó a {fila}{col+1}: {resultado}")
            break

# ///////////////////////
# INICIO DEL JUEGO
# //////////////////////
tablero_jugador = crear_tablero()
tablero_cpu = crear_tablero()
colocar_barcos(tablero_jugador)
colocar_barcos(tablero_cpu)

tiros_cpu = set()

print("¡Bienvenido a Batalla Naval!")
mostrar_tablero(tablero_jugador, "Jugador")
mostrar_tablero(tablero_cpu, "CPU", ocultar=True)

# //////////Bucle del juego//////////
while quedan_barcos(tablero_jugador) and quedan_barcos(tablero_cpu):
    #//////////// Turno del jugador/////////////
    while True:
        entrada = input("\nIngresa la coordenada para disparar (ej: A1 - E5): ").upper()
        if entrada_valida(entrada):
            fila, col = procesar_entrada(entrada)
            resultado = disparar(tablero_cpu, fila, col)
            print(f"Disparaste a {entrada}: {resultado}")
            break
        else:
            print("Entrada inválida. Usa letras A-E y números 1-5.")

    #/////////// Mostrar tableros////////////////
    mostrar_tablero(tablero_jugador, "Jugador")
    mostrar_tablero(tablero_cpu, "CPU", ocultar=True)

    # /////////Verificar si el jugador ganó//////////
    if not quedan_barcos(tablero_cpu):
        print("\n ¡Felicidades! Hundiste todos los barcos enemigos.")
        break

    # //////////Turno CPU////////////////////
    turno_cpu(tablero_jugador, tiros_cpu)

    # ////////Mostrar tablero del jugador tras disparo de la CPU//////////
    mostrar_tablero(tablero_jugador, "Jugador")

    #////////////// Verificar si la CPU ganó///////////////////
    if not quedan_barcos(tablero_jugador):
        print("\n La CPU ha hundido todos tus barcos. ¡Perdiste!")
        break










    