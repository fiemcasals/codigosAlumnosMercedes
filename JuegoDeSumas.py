import random

def jugar():
    vidas = 3
    puntos = 0
    cantidad_preguntas = 0

    print("\n🧠 ¡Comienza el juego de sumas!")
    print("Tenés 3 vidas. Perdés una cada vez que te equivocás.")

    while vidas > 0:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        resultado = num1 + num2

        print(f"\n¿Cuánto es {num1} + {num2}?")
        try:
            respuesta = int(input("Tu respuesta: "))
        except ValueError:
            print("⚠️ Eso no es un número. Perdés una vida.")
            vidas -= 1
            continue

        cantidad_preguntas += 1

        if respuesta == resultado:
            print("✅ ¡Correcto!")
            puntos += 1
        else:
            print(f"❌ Incorrecto. La respuesta era {resultado}.")
            vidas -= 1
            print(f"💔 Te quedan {vidas} vidas.")

    print("\n🎮 Fin del juego.")
    print(f"Respondiste {cantidad_preguntas} preguntas.")
    print(f"✅ Acertaste {puntos}. ❌ Fallaste {cantidad_preguntas - puntos}.")

def menu():
    while True:
        print("\n🎲 MENÚ PRINCIPAL")
        print("1. Jugar")
        print("2. Salir")
        opcion = input("Elegí una opción (1 o 2): ")

        if opcion == "1":
            jugar()
        elif opcion == "2":
            print("👋 ¡Gracias por jugar! Nos vemos.")
            break
        else:
            print("❌ Opción inválida. Probá de nuevo.")

# Ejecutamos el menú
menu()
