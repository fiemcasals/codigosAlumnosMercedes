import random

def crear_tablero():
    letras = ['A', 'B', 'C', 'D', 'E']
    numeros = ['1', '2', '3', '4', '5']
    tablero = {}
    for letra in letras:
        for numero in numeros:
            tablero[letra + numero] = 'O'  # Agua
    return tablero

def mostrar_tablero(tablero, ocultar_barcos=False):
    print("  A B C D E")
    for num in ['1', '2', '3', '4', '5']:  # Iteramos sobre las filas
        fila = num + " "  # Comienza la fila con el número de fila
        for letra in ['A', 'B', 'C', 'D', 'E']:  # Iteramos sobre las columnas
            val = tablero[letra + num]  # Obtenemos el valor de la celda correspondiente
            if ocultar_barcos and val == 'B':  # Si se debe ocultar el barco
                fila += 'O '  # Colocamos un agua (O) en lugar del barco
            else:
                fila += val + " "  # De lo contrario, mostramos el valor de la celda
        print(fila)  # Imprimimos la fila completa


def colocar_barcos_aleatorio(tablero, cantidad):
    posiciones_disponibles = list(tablero.keys())
    barcos = random.sample(posiciones_disponibles, cantidad)
    for pos in barcos:
        tablero[pos] = 'B'
    return barcos

def atacar(tablero, pos):
    if tablero.get(pos) == 'B':
        tablero[pos] = '💥'
        print("¡Impacto!")
        return True
    elif tablero.get(pos) == 'O':
        tablero[pos] = 'X'
        print("Agua.")
        return False
    elif tablero.get(pos) in ['X', '💥']:
        print("Ya atacaste ahí.")
        return False
    else:
        print("Coordenada inválida.")
        return False

def contar_barcos_restantes(tablero):
    return list(tablero.values()).count('B')

# Inicialización
tablero_jugador = crear_tablero()
tablero_cpu = crear_tablero()
barcos_jugador = colocar_barcos_aleatorio(tablero_jugador, 3)
barcos_cpu = colocar_barcos_aleatorio(tablero_cpu, 3)

turno = 1
while True:
    print("\n" + "="*30)
    print(f"🔁 Turno {turno}")
    print("\nTu tablero:")
    mostrar_tablero(tablero_jugador)
    print("\nTablero enemigo:")
    mostrar_tablero(tablero_cpu, ocultar_barcos=True)

    # Turno del jugador
    while True:
        ataque_jugador = input("\n📍 Tu ataque (ej: B3): ").upper()
        if ataque_jugador in tablero_cpu:
            impacto = atacar(tablero_cpu, ataque_jugador)
            break
        else:
            print("Coordenada inválida. Intentá de nuevo.")

    if contar_barcos_restantes(tablero_cpu) == 0:
        print("\n🎉 ¡Ganaste! Hundiste todos los barcos enemigos.")
        break

    # Turno de la CPU
    print("\n🤖 Turno del enemigo...")
    posibles = [k for k, v in tablero_jugador.items() if v in ['O', 'B']]
    ataque_cpu = random.choice(posibles)
    print(f"El enemigo ataca en {ataque_cpu}...")
    atacar(tablero_jugador, ataque_cpu)

    if contar_barcos_restantes(tablero_jugador) == 0:
        print("\n💀 Perdiste. El enemigo hundió todos tus barcos.")
        break

    turno += 1
