#Un juego de adivinanza funciona así:

#  La computadora tiene un número secreto entre 1 y 10 (por ahora, lo escribís vos fijo en el código, no hace falta que sea aleatorio).

#  El jugador tiene 3 intentos para adivinar el número.

#  En cada intento, el programa debe pedirle al usuario que ingrese un número.

# Si el número es correcto, el programa debe mostrar: "¡Correcto! Ganaste." y terminar.

# Si el número es incorrecto, debe decirle si el número ingresado es mayor o menor que el se
import random 
print('~~ Adivina el NUMERO ~~\n')
print('El numero estara entre el 1 y el 10')

n = random.randint(1, 10)
intentos = 3
restos = intentos

while intentos  > 0  :
    respuesta = int(input("ingrese el numero: "))

    if respuesta == n:
         print("Correcto, ganaste")
         break
    elif respuesta > n:
         print(" Es menor ")
         
    elif respuesta < n:
         print(" Es mayor ")
         
    else:
        print('pon un numero que sea valido')
        continue
    intentos -= 1

print(f'El numero era {n} ')



