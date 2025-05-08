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

#//////////////////////////////
#////SISTEMA DE TABLEROS///////
#/////////////////////////////
def crear_tablero():
    letras = list(string.ascii_uppercase[:5]) 
    return {letra: ["~"] * 5 for letra in letras}


def mostrar_tablero(tablero, nombre="Jugador", ocultar=False):
    print(f"\nTablero de {nombre}")
    print("  " + "".join([str(i+1).rjust(2) for i in range(5)])) 
    for fila in tablero:
        if ocultar:
            fila_mostrada = ["~ " if celda == "O" else celda for celda in tablero[fila]]
        else:
            fila_mostrada = tablero[fila]
        print(f"{fila}  " + " ".join(fila_mostrada))

#///////////////////////////
#//// SISTEMA DE BARCOS ///
#/////////////////////////
def colocar_barcos_de_una_casilla(tablero, cantidad=3):
    colocados = 0
    letras = list(tablero.keys())

    while colocados < cantidad:
        fila = random.choice(letras)
        col = random.randint(0, 4) 
        if tablero[fila][col] == "~":
            tablero[fila][col] = "O"
            colocados += 1

#///////VARIABLES//////////
#/////////////////////////
tablero_jugador = crear_tablero()
tablero_cpu = crear_tablero()

colocar_barcos_de_una_casilla(tablero_jugador)
colocar_barcos_de_una_casilla(tablero_cpu)

mostrar_tablero(tablero_jugador, "Jugador")
mostrar_tablero(tablero_cpu, "CPU", ocultar=False)






    