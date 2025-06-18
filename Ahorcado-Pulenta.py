import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_horca(intentos):
    horca = [
        "  +---+",
        "  |   |",
        "      |",
        "      |",
        "      |",
        "      |",
        "========="
    ]
    partes = [
        (2, 2, "O"),    # cabeza (dos espacios a la izquierda)
        (3, 2, "|"),    # cuerpo
        (3, 1, "/"),    # brazo izq
        (3, 3, "\\"),   # brazo der
        (4, 1, "/"),    # pierna izq
        (4, 3, "\\")    # pierna der
    ]
    for i in range(6 - intentos):
        fila, col, char = partes[i]
        horca[fila] = horca[fila][:col] + char + horca[fila][col+1:]
    for linea in horca:
        print(linea)

def mostrar_progreso(palabra, letras_adivinadas):
    progreso = [letra if letra in letras_adivinadas else "_" for letra in palabra]
    print("Palabra: " + " ".join(progreso))

def juego_ahorcado():
    palabra = input("Ingresá la palabra a adivinar: ").lower()
    limpiar_pantalla()
    letras_adivinadas = set()
    intentos = 6
    letras_erroneas = set()

    while intentos > 0:
        limpiar_pantalla()
        mostrar_horca(intentos)
        mostrar_progreso(palabra, letras_adivinadas)
        print(f"Letras incorrectas: {', '.join(sorted(letras_erroneas))}")
        letra = input("Ingresá una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Ingresá solo una letra.")
            input("Presioná Enter para continuar...")
            continue

        if letra in letras_adivinadas or letra in letras_erroneas:
            print("Ya ingresaste esa letra.")
            input("Presioná Enter para continuar...")
            continue

        if letra in palabra:
            letras_adivinadas.add(letra)
            if all(l in letras_adivinadas for l in palabra):
                limpiar_pantalla()
                mostrar_horca(intentos)
                mostrar_progreso(palabra, letras_adivinadas)
                print("¡Felicitaciones! ¡Adivinaste la palabra!")
                break
        else:
            letras_erroneas.add(letra)
            intentos -= 1
    else:
        limpiar_pantalla()
        mostrar_horca(intentos)
        print(f"¡Perdiste! La palabra era: {palabra}")

if __name__ == "__main__":
    juego_ahorcado()
    while True:
        jugar_nuevamente = input("¿Querés jugar de nuevo? (s/n): ").lower()
        if jugar_nuevamente != 's':
            break
        limpiar_pantalla()