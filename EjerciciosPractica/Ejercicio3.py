#Escribir una función que genere y retorne un diccionario ASCII. Para ello, las claves deben ser las letras 
#a partir de la 'a' y el valor debe ser el número ASCII (a -> 97, b -> 98, …). 

def generar_diccionario_ascii():
    diccionario = dict()
    for letra in range(ord('a'), ord('z') + 1):
        diccionario[chr(letra)] = letra
    return diccionario

# Ejemplo de uso:
ascii_diccionario = generar_diccionario_ascii()
print(ascii_diccionario)
