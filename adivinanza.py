import random

# Número secreto fijo o aleatorio
numero_secreto = random.randint(1, 10)
# numero_secreto = 7  # ← Usar este si querés que sea fijo para probar

intentos = 3

print("🎯 Bienvenido al juego de adivinanza. Tienes 3 intentos para adivinar el número secreto entre 1 y 10.")

for intento in range(1, intentos + 1):
    try:
        adivinanza = int(input(f"\nIntento {intento}: Ingresa un número entre 1 y 10: "))

        if adivinanza < 1 or adivinanza > 10:
            print("⚠️ El número debe estar entre 1 y 10. No pierdes intento, intenta de nuevo.")
            continue

        if adivinanza == numero_secreto:
            print("🎉 ¡Correcto! ¡Ganaste!")
            break
        elif adivinanza < numero_secreto:
            print("🔼 El número secreto es mayor.")
        else:
            print("🔽 El número secreto es menor.")

    except ValueError:
        print("❌ Entrada inválida. Por favor ingresa un número entero.")
        continue
else:
    print(f"\n💥 Perdiste. El número era {numero_secreto}.")
