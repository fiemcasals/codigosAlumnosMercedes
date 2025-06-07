import random
import os
import time
from colorama import Fore, Style, Back

# Inicializamos colorama para que funcione en Windows
#init()

class BatallaNaval:
    def __init__(self):
        pass

    def generar_tablero(self,condicion,cantidad_barcos):
        """Genera un tablero, la condicion 
        True devuelve el tablero relleno con las minas...
        False devuelve el tablero relleno solo con 0...
        cantidad de minas por defecto 3"""

        tablero=[]
        tamanio=0

        if cantidad_barcos == 3:
            tamanio=5
        else:
            tamanio=10
            
        for x in range(0,tamanio):
            tablero.append([])
            for y in range(0,tamanio):
                tablero[x].append(0)
        
        if condicion:
            i=0
            while i < cantidad_barcos:
                x = random.randint(0,tamanio-1)
                y = random.randint(1,tamanio-2)

                if tablero[x][y]!= 1 and tablero[x][y-1]!= 1 and tablero[x][y+1]!= 1:
                    tablero[x][y] = 1
                    i+=1
        
        return tablero
    """
    def mostrar_tablero(self,tablero): #Funcion original
        #Recibe un tablero echo por una lista de listas y lo imprime#
        for fila in tablero:
            print(fila)"""
    
    def mostrar_tablero(self,tablero,tamanio):
        """Crea un nuevo tablero reemplazando las lista de numeros por listas con un str echo de los numeros"""
        
        #Crear
        tablero2string=[]
        for x in range(0,tamanio):
            tablero2string.append([])
            letras = str("ABCDEFGHIJH")

            referencia = letras[x]
            referencia += str(" ")
            
            dato = referencia 
            espacio = " "
            for y in range(0,tamanio):
                dato += str(tablero[x][y]) + espacio   
            tablero2string[x].append(dato)
        
        #Imprimir
        for x in range(0,tamanio):
            nuevo_str = ""
            strin=""
            fila = tablero2string[x]
            largo = len(fila[0])
            string = fila[0]

            for pos in range(0,largo):
                
                if string[pos] == "1":
                    nuevo_str += Fore.GREEN + string[pos] + Style.RESET_ALL
                    #nuevo_str += "\033[32m" + strin[pos] +"\033[0m"
                elif string[pos] == "8":
                    nuevo_str += Fore.RED + string[pos] + Style.RESET_ALL
                elif string[pos] == "0":
                    nuevo_str += Fore.BLUE + string[pos] + Style.RESET_ALL
                else:    
                    nuevo_str += Fore.WHITE + string[pos] + Style.RESET_ALL
            print(nuevo_str)
        if tamanio == 5:
            print("  1 2 3 4 5 ")
        else:
            print("  1 2 3 4 5 6 7 8 9 10")

    def disparar(self,tablero_de_disparos,tablero1,tablero2,jugador,tamanio):
        """Recibe los 3 tableros, el tamanio del mapa, si esta disparando el jugador o la maquina"""
        if jugador:
            print("Es tu turno de disparar...")
            if tamanio == 5:
                lista_de_letras = ["a", "b", "c", "d", "e"]
                max_col = 5
            else:
                lista_de_letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
                max_col = 10

            # Fila como letra
            while True:
                try:
                    entradafila = input(f"Ingresa una coordenada para\nFila entre {Fore.YELLOW}{lista_de_letras[0].upper()}{Style.RESET_ALL}-{Fore.YELLOW}{lista_de_letras[-1].upper()}{Style.RESET_ALL}:-> ").lower()
                    if entradafila in lista_de_letras:
                        fila = lista_de_letras.index(entradafila)
                        break
                    else:
                        print("Coordenada incorrecta!!!")
                        time.sleep(2)
                except Exception:
                    print("Por favor, ingresa una letra válida.")
                    time.sleep(2)
            # Columna como número
            while True:
                try:
                    entradacolumna = input(f"Ingresa una coordenada para \nColumna entre {Fore.YELLOW}1{Style.RESET_ALL}-{Fore.YELLOW}{max_col}{Style.RESET_ALL}:-> ")
                    columna = int(entradacolumna) - 1
                    if 0 <= columna < max_col:
                        break
                    else:
                        print("Coordenada incorrecta!!!")
                        time.sleep(2)
                except ValueError:
                    print(f"Por favor, ingresa un número válido del 1 al {max_col}.")
                    time.sleep(2)

            time.sleep(1)
            if tablero1[fila][columna] == 0:
                print("Tu disparo fue al agua!")
                tablero_de_disparos[fila][columna] = 8
                tablero1[fila][columna] = 8
                time.sleep(2)
                return False
            elif tablero1[fila][columna] == 1:
                print("Acertaste!! Le diste a un barco!")
                tablero_de_disparos[fila][columna] = 1
                tablero1[fila][columna] = 0
                time.sleep(2)
                return True
            else:
                print("Ya disparaste a esa coordenada...")
                time.sleep(2)
                return None
        else:
            # Disparo de la maquina
            while True:
                fila = random.randint(0, tamanio-1)
                columna = random.randint(0, tamanio-1)
                if tablero2[fila][columna] != 8:
                    break
            if tablero2[fila][columna] == 0:
                self.animacion_disparo()
                print("El enemigo fallo!! Disparo al agua!")
                tablero2[fila][columna] = 8
                time.sleep(2)
                return False
            elif tablero2[fila][columna] == 1:
                self.animacion_disparo()
                print("El enemigo acerto!! Le dieron a un barco!")
                tablero2[fila][columna] = 0
                time.sleep(2)
                return True
                
    def animacion_disparo(self):
        print("Enemigo disparando!")
        caracter_a_añadir = "--"
        cadena = "-->"
        for i in range(0,4):
            print(cadena)
            cadena = caracter_a_añadir + cadena
            time.sleep(1)

    def mostrar_titulo_referencias(self):
        os.system("cls")
        print("*******************************")
        print("******** " + Fore.RED + "BATALLA NAVAL" + Style.RESET_ALL + " ********")
        print("*******************************")
        print("Ref: " + Fore.BLUE + "0" + Style.RESET_ALL + " agua, " + Fore.GREEN + "1" + Style.RESET_ALL + " barco, " + Fore.RED + "8" + Style.RESET_ALL + " fallido")
        print("    ")
         
    def pantalla_de_seleccion_del_tablero(self):

        respuesta=0
        while respuesta != 1 and respuesta != 2:
            
            self.mostrar_titulo_referencias()

            time.sleep(1)
            print("Bienvenido al clasico juego de \nla batalla naval...")
            time.sleep(2)
            print("    ")
            print("Vamos a elegir el tamaño del \nmapa...")
            time.sleep(2)
            print("    ")
            print("Ingrese " + Fore.BLUE +"'1'" + Style.RESET_ALL + " para un tamaño de \n5x5 con 3 barcos...")
            print("    ")
            time.sleep(2)
            print("Ingrese " + Fore.BLUE +"'2'" + Style.RESET_ALL + " para un tamaño de \n10x10 con 5 barcos...")
            print("    ")
            time.sleep(2)

            entrada = input("Ingrese aqui: --> ")
            try:
                respuesta = int(entrada)
                if respuesta not in [1, 2]:
                    print("Opcion ingresada incorrecta...")
                    time.sleep(2)
            except ValueError:
                print("Por favor, ingrese un número válido 1 o 2.")
                time.sleep(2)
        
        return respuesta
        
    def comprobar_fin_de_juego(self,vida_jugador,vida_maquina):

        self.mostrar_titulo_referencias()
        print("    ")
        print(f"Barcos del Jugador {vida_jugador}")
        print("    ")
        print(f"Barcos del Enemigo {vida_maquina}")
        print("    ")

        if vida_jugador == 0 or vida_maquina == 0:
            if vida_jugador == 0:
                print("*******************************")
                print("********  "+ Fore.RED + "Perdiste!!!" + Style.RESET_ALL + "  ********")
                print("*******************************")
            elif vida_maquina == 0:
                print("*******************************")
                print("********  "+ Fore.YELLOW + "Ganaste!!!" + Style.RESET_ALL + "   ********")
                print("*******************************")
            return True
        else:
            return False
        
         
########################  Flujo del programa ####################### 

#Instanciamos la clase y la llamamos juego
juego = BatallaNaval()

respuesta = juego.pantalla_de_seleccion_del_tablero()

if respuesta == 1:
    cantidad_barcos = 3
    tamanio_del_tablero = 5
else:
    cantidad_barcos = 5
    tamanio_del_tablero = 10

#Enemigo
tablero1 = juego.generar_tablero(True,cantidad_barcos)
vida_maquina = cantidad_barcos

#Tablero para los disparos realizados
tablero_disparos = juego.generar_tablero(False,cantidad_barcos)

#Jugador
tablero2 = juego.generar_tablero(True,cantidad_barcos)
vida_jugador = cantidad_barcos

#Bucle principal
while vida_maquina > 0 and vida_jugador > 0:
    time.sleep(2)
    juego.mostrar_titulo_referencias()
    
    print(Back.WHITE + Fore.YELLOW + "  Este es el tablero enemigo  " + Style.RESET_ALL)
    juego.mostrar_tablero(tablero_disparos,tamanio_del_tablero)
    #print("  1 2 3 4 5 6 7 8 9 10")
    
    print(Back.WHITE + Fore.YELLOW + "      Este es tu tablero      " + Style.RESET_ALL)
    juego.mostrar_tablero(tablero2,tamanio_del_tablero)
    #
    
    #Disparo del jugador
    jugador = True
    disparo = juego.disparar(tablero_disparos,tablero1,tablero2,jugador,tamanio_del_tablero)
    
    if disparo == True:
        vida_maquina-=1

    #Disparo de la maquina
    jugador = False
    disparo = juego.disparar(tablero_disparos,tablero1,tablero2,jugador,tamanio_del_tablero)

    if disparo == True:
        vida_jugador-=1

    #Fin del juego
    #Comprueba si le quedan vidas a los jugadores y las muestra
    fin_del_juego=juego.comprobar_fin_de_juego(vida_jugador,vida_maquina)

    #Si alguien se quedo sin vidas muestra los tableros
    if fin_del_juego:
        
        juego.mostrar_titulo_referencias()

        print(Back.WHITE + Fore.YELLOW + "  Este es el tablero enemigo  " + Style.RESET_ALL)
        juego.mostrar_tablero(tablero1,tamanio_del_tablero)

        print("    ")

        print(Back.WHITE + Fore.YELLOW + "      Este es tu tablero      " + Style.RESET_ALL)
        juego.mostrar_tablero(tablero2,tamanio_del_tablero)

        print("    ")

        print("Fin del juego!!!")
        print("Gracias por jugar, para salir presione 'Enter'...")
        input()
        break
  
    time.sleep(2)

