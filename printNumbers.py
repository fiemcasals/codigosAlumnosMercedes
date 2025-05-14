import time
import random

def imprimir_numeros_especiales(inicio, fin):
    resultado = []

    for i in range(inicio, fin + 1):
        if i % 7 == 0 and i % 5 != 0:
            resultado.append(str(i))

    print("\n🥁 Redoble de tambores... Calculando tus números mágicos...\n")
    time.sleep(random.uniform(1.2, 2.0))  # Simula "suspenso"

    if resultado:
        print("✨ ¡Estos son tus números especiales, mágicamente únicos! ✨")
        print('🎯 ' + ', '.join(resultado))
    else:
        print("😢 Oh no... no hay números especiales en ese rango.")
        print("¡Probá otro rango! Capaz la suerte cambia. 🍀")

    return resultado  


def pedir_rango_y_mostrar():
    while True:
        try:
            print("\n🎲 ¡Bienvenido al selector de números especiales! 🎲")
            inicio = int(input("📥 Ingresá el número de inicio (entre 1 y 100): "))
            fin = int(input("📥 Ingresá el número de fin (entre 1 y 100): "))

            if not (1 <= inicio <= 100 and 1 <= fin <= 100):
                print("🚫 Los números deben estar entre 1 y 100. ¡Jugá limpio! 😅")
                continue

            if inicio > fin:
                print("⚠️ El inicio debe ser menor o igual al fin. ¿Estamos haciendo trampa? 😄")
                continue

            imprimir_numeros_especiales(inicio, fin)

            jugar_otra_vez = input("\n¿Querés intentarlo de nuevo con otro rango? (s/n): ").strip().lower()
            if jugar_otra_vez != 's':
                print("👋 ¡Gracias por jugar! Nos vemos en la próxima aventura numérica.")
                break

        except ValueError:
            print("🙈 Eso no fue un número válido. Intentá con un número entero, porfa.")

# ¡Que empiece el juego!
pedir_rango_y_mostrar()
