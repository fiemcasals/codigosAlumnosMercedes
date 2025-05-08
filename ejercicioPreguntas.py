import random  # Importamos el módulo random para generar números aleatorios

# Función que genera una pregunta aleatoria de suma
def generar_pregunta():
    a = random.randint(1, 20)  # Genera un número aleatorio entre 1 y 20
    b = random.randint(1, 20)  # Genera otro número aleatorio entre 1 y 20
    resultado = a + b  # Calcula la suma
    return f"¿Cuánto es {a} + {b}?", resultado  # Devuelve la pregunta como texto y el resultado

# Función principal del juego
def juego_sumas():
    puntaje = 0  # Puntaje inicial

    
    print("¡Bienvenido al juego de sumas básicas!")
    print("Reglas: +10 puntos por cada respuesta correcta, -5 por cada incorrecta.")
    print("¡Debes llegar a 50 puntos para ganar!\n")

    
    while puntaje < 50:
        pregunta, respuesta_correcta = generar_pregunta()  # Genera una nueva pregunta utilizando destructuring
        print(pregunta)  # Muestra la pregunta

        try:
            respuesta = int(input("Tu respuesta: "))  # Solicita respuesta del usuario
        except ValueError:
            print("Por favor, ingresa un número válido.\n")  # Maneja errores de entrada
            continue  # Vuelve al inicio del bucle

        # Comprobación de respuesta
        if respuesta == respuesta_correcta:
            puntaje += 10  
            print("✅ ¡Correcto! +10 puntos.")
        else:
            puntaje -= 5  
            print(f"❌ Incorrecto. La respuesta era {respuesta_correcta}. -5 puntos.")

        print(f"Puntaje actual: {puntaje}\n") 

        
        if puntaje < 50:
            seguir = input("¿Querés seguir jugando? (s/n): ").lower()
            if seguir != 's':
                print("Juego finalizado. Tu puntaje final fue:", puntaje)
                return  # Termina el juego

   
    print("🎉 ¡Felicidades! Alcanzaste los 50 puntos. ¡Ganaste!")


juego_sumas()
