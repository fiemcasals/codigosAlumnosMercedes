#batalla nabal
# del a al e y del 1 al 5
#crear tablero que son 2
#colocar naves (tablero,simbolo ) a si ppone mis naves y e de enemigo
#filas 5 y naves 3
#randint es fils y choise columnas

#mostrar tablero


#diagrama listo
#defino cantidad de filas y columnas 
#filas 5 y columnas a al e 
#definir que  simbolos x= hundido y o= agua 

#naves son 3
#creo objeto osea definir la variable mapa
#diccionario con clave y valor pero necesito
#diccionariio mas complicado osea un diccionario dentro de otro diccionario
#tiene llave {}claves y un valor 
#el valor va a ser un diciionario 
# {clave:valor}

import random


print("Bienvenido a Batalla Naval \n")

respuesta=input("comenzamos con el juego? si/salir: ").lower()

if respuesta == "salir":
    print("finalizaste el juego")
   
elif respuesta =="si":
    print("¡Comencemos el juego!")
    nombre_jugador1 = input("Ingrese el nombre del 'jugador' 1: \n")
    nombre_jugador2 = input("Ingrese el nombre del 'jugador' 2: \n")
    FILAS =int(input( "Ingrese la cantidad de filas:  "))
    COLUMNAS = int(input("Ingrese la cantidad de columnas:  \n"))
    NAVES = 3
    PRUEBA = 1
    
    MAPA_INICIAL_MIO= [[" . " for _ in range(COLUMNAS)] for _ in range (FILAS)] 
    MAPA_INICIAL_ENEMIGO= [[" - " for _ in range(COLUMNAS)] for _ in range (FILAS)]
    naves_random = set()
    while len(naves_random) < NAVES:
         fil = random.randint(0, FILAS - 1 )
         col = random.randint(0, COLUMNAS - 1)
         naves_random.add((fil, col))
    
    LETRAS = []
    for i in range(COLUMNAS):
       letras = input("ingrese la letra que quiere en la columna: ").upper()
       LETRAS.append(letras)
       
    def mostrar_MAPA_mio(MAPA_INICIAL_MIO):
     for i in range (PRUEBA):
          print("   " + "   ".join(LETRAS))
          for i, fila in enumerate(MAPA_INICIAL_MIO):
            print(f"{i+1} " + " ".join(fila))

    def mostrar_MAPA_enemigo(MAPA_INICIAL_ENEMIGO):
         print("   " + "   ".join (LETRAS))
         for i, fila in enumerate(MAPA_INICIAL_ENEMIGO):
            print(f"{i+1} " + " ".join(fila))
     
    mostrar_MAPA_mio(MAPA_INICIAL_MIO)
    print("ya elegiste tus letras y numeros \n")
    print ("comenzamos \n")
   
    turno = 1
 
    while True:
      if turno == 1:
            
             print(f" {nombre_jugador1} dispara al lugar que quieras \n")
             tiro_fil = input("pone el numero: ")
             tiro_col = input ("pone la columna: ").upper()
             if tiro_col not in LETRAS or not(1<= int(tiro_fil) <= 5): 
               print("invalido")
               continue

             columna = ord(tiro_col) - ord("A") 
             fila = int(tiro_fil) - 1
        
             if (fila, columna) in naves_random :
               MAPA_INICIAL_MIO[fila][columna] = " x " 
               mostrar_MAPA_mio(MAPA_INICIAL_MIO)
               print("hundiste una nave")
               naves_random.remove((fila, columna))
               print(MAPA_INICIAL_MIO)
               print("naves restantes: ", len(naves_random))
               mostrar_MAPA_mio(MAPA_INICIAL_MIO)
               
             elif (columna, fila) not in naves_random:
              
              MAPA_INICIAL_MIO[fila][columna] = " ~ "
              mostrar_MAPA_mio(MAPA_INICIAL_MIO)
              print(" 'Agua' ")

             else:
              if naves_random == 0:
                 print("has hundido todas las naves")
            
      elif turno == 2:
          
            print(f"\n {nombre_jugador2} dispara al lugar que quieras\n")
            mostrar_MAPA_enemigo(MAPA_INICIAL_ENEMIGO)
            tiro_fil_enemigo = input("pone el numero: ")
            tiro_col_enemigo = input ("pone la columna: ").upper()
            if tiro_col_enemigo not in LETRAS or not(1<= int(tiro_fil_enemigo) <= 5): 
               print("invalido")
               continue
            columna_enemigo = ord(tiro_col_enemigo) - ord("A") 
            fila_enemigo = int(tiro_fil_enemigo) - 1

            if (fila_enemigo, columna_enemigo) in naves_random:
              
               MAPA_INICIAL_ENEMIGO[fila_enemigo][columna_enemigo]= " x "
               mostrar_MAPA_enemigo(MAPA_INICIAL_ENEMIGO)
               print("Jugador 2 hundiste una nave")
               naves_random.remove((columna_enemigo, fila_enemigo))
               print("naves restantes: ", len(naves_random))

            elif(fila_enemigo,columna_enemigo) not in naves_random:
            
             MAPA_INICIAL_ENEMIGO[fila_enemigo][columna_enemigo] = " ~ "
             mostrar_MAPA_enemigo(MAPA_INICIAL_ENEMIGO)
             print(" 'Agua' ")
            else:
              if naves_random == 0:
                 print("has hundido todas las naves")
        
      turno = 2 if turno == 1 else 1
          
         

    
 
