#Un juego de adivinanza funciona así:

#La computadora tiene un número secreto entre 1 y 10 (por ahora, lo escribís vos fijo en el código, no hace falta que sea aleatorio).
#El jugador tiene 3 intentos para adivinar el número.
#En cada intento, el programa debe pedirle al usuario que ingrese un número.
#Si el número es correcto, el programa debe mostrar: "¡Correcto! Ganaste." y terminar.
#Si el número es incorrecto, debe decirle si el número ingresado es mayor o menor que  el secreto.
#Si se agotan los 3 intentos, el programa debe decir: "Perdiste. El número era X.


import random #Importando modulo random

numero_secreto = random.randint(1 , 10) #Numero secreto random que comprende entre 1 y 10a
intentos = 4
ganaste = False

while intentos > 1 and not ganaste: 
    try:
        numero = int(input (f"Intento {intentos - 1}: Ingresá un número entre 1 y 10: "))
        intentos -= 1

        if numero == numero_secreto:
            print("¡Correcto! Ganaste.")
            ganaste = True
        elif numero < numero_secreto:
            print("El número es mayor.")
        else:
            print("El número es menor.")
            
    except ValueError:
            print("ingrese un numero valido")

if not ganaste:
    print(f"Perdiste. El número era {numero_secreto}.")


    




   
        
    



    




