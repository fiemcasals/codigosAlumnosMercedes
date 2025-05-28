

import random 

tablero = [[0 for i in range(5)] for j in range(5)]
barcos = 3
barcos_colocados = 0
disparos = 15



while barcos_colocados < barcos: # colocar_barcos_sin_repetir_posicion
    fila = random.randint(0, 4)
    columna = random.randint(0, 4)
    
    if tablero[fila][columna] == 0:
        tablero[fila][columna] = 1
        barcos_colocados += 1
        


def ver_tablero_oculto(tablero): #def_ver_tablero
    print("Tablero:")
    for fila in tablero:
        linea = ""
        for celda in fila:
            if celda == 0:
                linea += ". "
            elif celda == -1:
                linea += "O "
            elif celda == -2:
                linea += "X "
            else:
                linea += ". " 
        print(linea)
    print()

def jugar(tablero, disparos):
    for i in range(disparos):
        print(f"Intento {i+1} de {disparos}")
        ver_tablero_oculto(tablero)
        
        try:
            fila = int(input("Ingrese la fila (0-4): "))
            columna = int(input("Ingrese la columna (0-4): "))
        except ValueError:
            print("Entrada inválida. Usa solo números.")
            continue
        
        if fila < 0 or fila > 4 or columna < 0 or columna > 4:
            print("Posición inválida, fuera del tablero.")
            continue
        
        if tablero[fila][columna] == 1:
            print("Acertaste el disparo a una nave")
            tablero[fila][columna] = -2  
        elif tablero[fila][columna] in [-1, -2]:
            print("Ya disparaste en esa posición.")
        else:
            print("Agua")
            tablero[fila][columna] = -1  

        #verif_barcos
        if sum(sum(1 for celda in fila if celda == 1) for fila in tablero) == 0:   #verificar_barcos
            ver_tablero_oculto(tablero)
            print("¡Ganaste! ¡Encontraste todos los barcos!")
            return
    
    print("Perdiste, no te quedan disparos.")
    ver_tablero_oculto(tablero)

def main():
    print("francisco_romero_practica_1")
    print("Bienvenido a la Batalla Naval")
    print("Tenes 15 intentos para encontrar las naves, si te quedas sin disparos perdes.")
    jugar(tablero, disparos)


main()