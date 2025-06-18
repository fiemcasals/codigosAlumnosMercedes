# Juego del ahorcado, donde se ingresa una palabra por teclado y el otro jugador intenta adivinarla letra por letra. Se cuenta con 6 intentos.
import os
def jugar_ahorcado():
    print("¡Bienvenido al juego del ahorcado!")
    palabra = input("Ingresa una palabra: ")
    letras_adivinadas = []
    intentos = 6
    
    # Limpiar la pantalla para ocultar la palabra ingresada
    os.system('cls' if os.name == 'nt' else 'clear')  #
    while intentos > 0:
        letra = input("Adivina una letra: ")
        if letra in palabra:
            letras_adivinadas.append(letra)
            print("¡Correcto!")
        else:
            intentos -= 1
            print("Incorrecto. Te quedan", intentos, "intentos.")

        # Mostrar progreso
        progreso = ""
        for letra_palabra in palabra:
            if letra_palabra in letras_adivinadas:
                progreso += letra_palabra
            else:
                progreso += "_"
        print("Progreso:", progreso)

        if "_" not in progreso:
            print("¡Felicitaciones! Adivinaste la palabra:", palabra)
            break
    else:
        print("¡Perdiste! La palabra era:", palabra)
if __name__ == "__main__":
    jugar_ahorcado()    