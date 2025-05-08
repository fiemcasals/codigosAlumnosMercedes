#   Un juego de adivinanza funciona así:

#    La computadora tiene un número secreto entre 1 y 10 (por ahora, lo escribís vos fijo en el código, no hace falta que sea aleatorio).

#   El jugador tiene 3 intentos para adivinar el número.

#    En cada intento, el programa debe pedirle al usuario que ingrese un número.

#   Si el número es correcto, el programa debe mostrar: "¡Correcto! Ganaste." y terminar.

#   Si el número es incorrecto, debe decirle si el número ingresado es mayor o menor que  el secreto.

#   Si se agotan los 3 intentos, el programa debe decir: "Perdiste. El número era X."
import random

# Número secreto fijo
numero_secreto = random.randint(1, 10)

# El jugador tiene 3 intentos
intentos = 3

for intento in range(intentos):
    # Pedimos al usuario que ingrese un número
    adivinanza = int(input("Adivina el numero (entre 1 y 10): "))


    if adivinanza == numero_secreto:
        print("¡Correcto! Ganaste!.")
        break
    elif adivinanza < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
else:
    print(f"Perdiste. El número era {numero_secreto}.")
