"""
Un juego de adivinanza funciona así:
La computadora tiene un número secreto entre 1 y 10 (por ahora, lo escribís vos fijo en el código, no hace falta que sea aleatorio).
El jugador tiene 3 intentos para adivinar el número.
En cada intento, el programa debe pedirle al usuario que ingrese un número.
Si el número es correcto, el programa debe mostrar: "¡Correcto! Ganaste." y terminar.
Si el número es incorrecto, debe decirle si el número ingresado es mayor o menor que el secreto.
Si se agotan los 3 intentos, el programa debe decir: "Perdiste. El número era X."
"""

import random

def adivinanza(respuesta, intentos=3):
    while intentos > 0:
        valor = int(input(f"Ingresa un numero, tenes {intentos} intentos: "))
        if valor == respuesta:
            print("Correcto! ganaste")
            intentos = 0
        else:
            intentos -= 1

    print("Te quedaste sin intentos")

respuesta = random.randint(1, 10)
print("Adivina el numero secreto (entre 1 y 10)\n")
adivinanza(respuesta)
