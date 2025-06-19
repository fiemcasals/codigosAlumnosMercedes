"""
Piedra papel o tijera
"""
import random

def elegir_opciones(opciones):
    jugador1 = input("Elegi (piedra|papel|tijera): ")
    jugador2 = random.choice(opciones)
    return jugador1, jugador2

def determinar_ganador(jugador1, jugador2):
    """
    return 0 si Gano, 1 si perdio, 2 si empato

    """
    como_ganar = {"piedra": "tijera",
                  "papel": "piedra",
                  "tijera": "papel"}

    if jugador1 == jugador2:
        return 2

    # esto nos da a quien le gana la eleccion del jugador 1, si es igual a lo que eligio el jugador2
    # significa que gano el 1, de lo contrario perdio
    if como_ganar[jugador1] == jugador2:
        return 0
    else:
        return 1

def main():
    opciones = ["piedra", "papel", "tijera"]
    intentos = 3
    gano_1, gano_2 = 0, 0
    print("Piedra Papel o Tijera\n")
    
    # al mejor de 3
    while intentos > 0:

        print(f"Intentos restantes: {intentos}")
        j1, j2 = elegir_opciones(opciones)
        resultado = determinar_ganador(j1, j2)
        resultados = {0: "Gano", 1: "Perdio", 2: "Empato"}

        print(f"Jugador 1 eligio: {j1}, Jugador 2 eligio: {j2}\n")
        print(f"Jugador 1: {resultados[resultado]}")

        if resultados[resultado] == "Empato":
            continue
        if resultados[resultado] == "Gano":
            gano_1 += 1
        else:
            gano_2 += 1

        print(f"Ganadas j1: {gano_1}")
        print(f"Ganadas j2: {gano_2}\n")
        intentos -= 1

        if gano_1 >= 2:
            ganador = 1
        elif gano_2 >= 2:
            ganador = 2

        # con ganar 2 alcanza
        if gano_1 >= 2 or gano_2 >= 2:
            print(f"Gano el jugador {ganador}!")
            break

if __name__ == "__main__":
    main()
