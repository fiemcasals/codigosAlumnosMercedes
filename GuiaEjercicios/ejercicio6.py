# Se necesita un programa que reciba por línea de comando una serie de palabras, hasta que reciba la palabra "exit". Una vez recibida dicha instrucción, debe mostrar por salida standard las mismas palabras ingresadas, almacenadas en una lista, pero ordenadas alfabéticamente y cada una debe estar capitalizada.
# Resultado Esperado: El programa le solicita al usuario que ingrese y este escribe:
# Ingrese palabra: hola
# Ingrese palabra: QUE
# Ingrese palabra: tal
# Ingrese palabra: como
# Ingrese palabra: estas
# Ingrese palabra: exit
# Se espera recibir el siguiente resultado: ['Como', 'Estas', 'Hola', 'Que', 'Tal']

palabras = []  # inicializo la lista vacía

while True: # ciclo infinito
    palabra = input("Ingrese palabra: ")
    if palabra.lower() == "exit":
        break
    palabras.append(palabra) #si no se escribe exit, se guarda la palabra en la lista palabras

palabras.sort()  # Ordena la lista alfabéticamente
palabras = [palabra.capitalize() for palabra in palabras]  # capitalize() convierte la primera letra un string a mayúscula y el resto a minúscula


print(palabras) 