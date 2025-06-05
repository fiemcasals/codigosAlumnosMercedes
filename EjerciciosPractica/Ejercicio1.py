#Escribir una función que reciba como parámetros el inicio y fin (inclusive) de un rango numérico. La 
#función debe: 
#a. Imprimir en pantalla todos aquellos números que sean divisibles por 7 pero no sean divisibles 
#por 5.  
#b. Imprimir el mismo resultado anterior, pero separados por coma. 
 #Resultado Esperado: Por ejemplo, si se invoca con los parámetros 1 y 100 (puntos a y b) 
 #7 
#14 
#21 
#28 
#42 
#49 
#56 
#63 
#77 
#84 
#91 
#98 
#7,14,21,28,42,49,56,63,77,84,91,98

def numeros_divisibles(inicio, fin):
    # Lista para guardar los números que cumplen la condición
    resultado = []

    # Recorrer el rango
    for numero in range(inicio, fin + 1):
        if numero % 7 == 0 and numero % 5 != 0:
            print(numero)  # Punto a
            resultado.append(str(numero))  # Guardamos como string para usar luego en el join

    # Punto b: imprimir separados por coma
    print(",".join(resultado))

# Ejemplo de uso:
numeros_divisibles(1, 100)
