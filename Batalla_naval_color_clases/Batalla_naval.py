
import random
import os
import time

def generar_tablero():
  tablero1=[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
  ]
  i=0
  while i < 3:
    x = random.randint(0,4)
    y = random.randint(0,4)
    if tablero1[x][y]!= 1:
      tablero1[x][y] = 1
      i+=1
  return tablero1
  
def devolver_tablero_vacio():
  tablero=[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
  ]
  return tablero

def mostrar_tablero(tablero):
  for num in tablero:
    print(num)
    
def disparar(fila,columna,jugador):
  if jugador == 1:
    if maquina[fila][columna] == 0:
      print("Tu disparo fue al agua...")
      tablero_disparos[fila][columna] = 8
      maquina[fila][columna] = 8
    elif maquina[fila][columna] == 1:
      print("Acertaste!! Le diste a un barco!")
      tablero_disparos[fila][columna] = 1
      maquina[fila][columna] = 0
      return True
    else:
      print("Ya disparaste a esa coordenada...")
  else:
    time.sleep(2)
    if jugador1[fila][columna] == 0 and jugador1[fila][columna] != 8:
      print("El disparo del enemigo fue al agua...")
      jugador1[fila][columna] = 8
    elif jugador1[fila][columna] == 1 and jugador1[fila][columna] != 8:
      print("El enemigo acerto!! Le dieron a un barco!")
      jugador1[fila][columna] = 0
      return False

vida_jugador = 3
vida_maquina = 3
jugador1 = generar_tablero()
maquina = generar_tablero()
tablero_disparos = devolver_tablero_vacio()
fila = 5
columna = 5

#juego
while vida_maquina > 0 and vida_jugador > 0:
  print("    ")
  print("****** BATALLA NAVAL ******        Ref: 0 es agua, 1 es barco, 8 es disparo fallido")
  print("    ")
  print("Este es el tablero enemigo:")
  mostrar_tablero(tablero_disparos)
  print("    ")
  print ("Este es tu tablero:")
  mostrar_tablero(jugador1)
  print("    ")
  
  #disparo jugador
  print("Es tu turno de disparar...")
  fila=int(input("Ingresa una coordenada para fila 0-4..."))
  columna=int(input("Ingresa una coordenada para la columna 0-4..."))

  if disparar(fila,columna,1) == True:
    vida_maquina-=1
   
  #disparo de la maquina
  fila=random.randint(0,4)
  columna=random.randint(0,4)

  if disparar(fila,columna,2) == False:
    vida_jugador-=1
  
  print("    ")
  print(f"Barcos del J1 {vida_jugador}")
  print(f"Barcos del enemigo {vida_maquina}")
  print("    ")

  if vida_jugador == 0 or vida_maquina == 0:
    os.system("cls")
    break

  time.sleep(5)
  os.system("cls")

# Fin del juego
print("    ")
print("****** BATALLA NAVAL ******        Ref: 0 es agua, 1 es barco, 8 es disparo fallido")
print("    ")
if vida_jugador == 0:
  print("                        +++++++++++++++++++++++++")
  print("                        +++++  Perdiste!!!  +++++")
  print("                        +++++++++++++++++++++++++")
elif vida_maquina == 0:
  print("                        +++++++++++++++++++++++++")
  print("                        +++++  Ganaste!!!   +++++")
  print("                        +++++++++++++++++++++++++")

print(f"Barcos del J1 {vida_jugador}")
print(f"Barcos del enemigo {vida_maquina}")
print("    ")
print("Este es el tablero enemigo:")
mostrar_tablero(maquina)
print("    ")
print ("Este es tu tablero:")
mostrar_tablero(jugador1)
print("    ")
print("Fin del juego")
print("Gracias por jugar")
