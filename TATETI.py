import random
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Bienvenido al juego del TATETI ')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n')

tablero = [' ' for i in range(9)]

def mostrar_tablero():
    print("Tablero:\n")
    filas = []
    for i in range(3):
        
        filas.append("_|_".join(tablero[i*3:i*3+3]))
    print("\n".join(filas))#se pone salto de linea para que se forme un tablero


def verificar_empate():
    return ' ' not in tablero

def ganador (jugador):
     lineas_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]    
     ]
     for linea in lineas_ganadoras:
        if all(tablero[pos] == jugador for pos in linea):
     # En el contexto de la función ganador, 
     # se usa para verificar si todas las posiciones de una 
     # línea ganadora pertenecen al mismo jugador.(explicacion del pos)
            return True
     return False


turno = random.randint(1, 2) 
while True:
 mostrar_tablero()

 if turno == 1:
    print("\nEs tu turno jugador X\n")
    jugador= input("Ingrese un número del 1 al 9: ")
    if tablero[int(jugador) - 1] == ' ':
        tablero[int(jugador) - 1] = 'X'
        if ganador('X'):
            mostrar_tablero()
            print('\n Jugador ~~ X ~~ has ganado el juego\n')
            break
        elif verificar_empate():
            mostrar_tablero()
            print('\nAcabas de hacer un empate\n')
            break
        turno = 2
    else:
        print("\nPosición ocupada, elige otra.\n")

    if jugador == ganador:
     print('\nX has ganado el juego\n')


 elif turno == 2:
      print("\nEs tu turno jugador O\n")
      jugador= input(" x ingrese un numero del 1 al 9: ")
      if tablero[int(jugador) - 1] == ' ':
          tablero[int(jugador) - 1] = 'O'
          if ganador('O'):
              mostrar_tablero()
              print('\n Jugador ~~ O ~~ has ganado el juego')
              break
          elif verificar_empate():
                mostrar_tablero()
                print('\n Dio EMPATE, se termino el juego \n')
                break
          mostrar_tablero()
          turno = 1
      else:
          print("Posición ocupada, elige otra.")


 