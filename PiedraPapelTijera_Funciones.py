# Juego de piedra papel o tijera, donde el usuario juega contra la computadora. Elige una opción (1, 2 o 3 respectivamente) y compite contra la IA. Al mejor de 3 rondas, se determina el ganador final. Implementado con funciones para mejorar el código.

import random

def jugar_ronda():
    opciones = {1: "Piedra", 2: "Papel", 3: "Tijera"}
    puntaje_usuario = 0
    puntaje_computadora = 0

    while puntaje_usuario < 2 and puntaje_computadora < 2:
        print("\nElegí una opción:")
        for clave, valor in opciones.items():
            print(f"{clave}: {valor}")

        try:
            eleccion_usuario = int(input("Elegiste (1, 2 o 3): "))
            if eleccion_usuario not in opciones:
                print("Opción no válida. Intentalo de nuevo.")
                continue
        except ValueError:
            print("Entrada no válida. Por favor, ingresá un número (1,2 o 3).")
            continue

        eleccion_computadora = random.randint(1, 3)
        print(f"\nLa IA eligió: {opciones[eleccion_computadora]}")

        if eleccion_usuario == eleccion_computadora:
            print("¡Empate!")
        elif (eleccion_usuario == 1 and eleccion_computadora == 3) or \
             (eleccion_usuario == 2 and eleccion_computadora == 1) or \
             (eleccion_usuario == 3 and eleccion_computadora == 2):
            print("¡Ganaste esta ronda!")
            puntaje_usuario += 1
        else:
            print("¡La IA ganó esta ronda!")
            puntaje_computadora += 1

        print(f"Puntaje - Vos: {puntaje_usuario}, IA: {puntaje_computadora}")

    if puntaje_usuario > puntaje_computadora:
        print("\n¡Felicitaciones! Ganaste el juego.")
    else:
        print("\nLa IA ganó el juego. ¡Intentalo de nuevo!")
def iniciar_juego():
    print("¡Juego de Piedra, Papel o Tijera!")
    print("Al mejor de 3 rondas, el primero en llegar a 2 puntos gana.")
    jugar_ronda()
if __name__ == "__main__":
    iniciar_juego()
