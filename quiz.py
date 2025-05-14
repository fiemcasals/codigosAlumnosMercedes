import random  # Importamos el módulo random para generar números aleatorios

# Función que genera una pregunta aleatoria de suma
def generar_pregunta():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    resultado = a + b
    return f"¿Cuánto es {a} + {b}?", resultado

# Función principal del juego
def juego_sumas():
    puntaje = 0
    objetivo = 50

    print("🧮 ¡Bienvenido al juego de sumas básicas!")
    print("🎯 Reglas: +10 puntos por cada respuesta correcta, -5 por cada incorrecta.")
    print(f"🏆 ¡Debes llegar a {objetivo} puntos para ganar!\n")

    while puntaje < objetivo:
        pregunta, respuesta_correcta = generar_pregunta()
        print(pregunta)

        try:
            respuesta = int(input("Tu respuesta: "))
        except ValueError:
            print("⚠️ Por favor, ingresa un número válido.\n")
            continue

        if respuesta == respuesta_correcta:
            puntaje += 10
            print("✅ ¡Correcto! +10 puntos.")
        else:
            puntaje -= 5
            if puntaje < 0:
                puntaje = 0
            print(f"❌ Incorrecto. La respuesta era {respuesta_correcta}. -5 puntos.")

        print(f"📊 Puntaje actual: {puntaje} / {objetivo}")
        print(f"💡 Te faltan {objetivo - puntaje} puntos para ganar.\n")

        if puntaje < objetivo:
            seguir = input("¿Querés seguir jugando? (s/n): ").strip().lower()
            if seguir != 's':
                if puntaje >= objetivo * 0.8:
                    print("✨ Estuviste muy cerca. ¡Buen intento!")
                print("👋 Juego finalizado. Tu puntaje final fue:", puntaje)
                return

    print("🎉 ¡Felicidades! Alcanzaste los 50 puntos. ¡Ganaste!")

# Ejecutar el juego
juego_sumas()
