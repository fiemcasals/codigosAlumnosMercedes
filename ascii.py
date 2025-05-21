"""
3. 
Escribir una función que genere y retorne un diccionario ASCII. Para ello, las claves deben ser las letras
a partir de la 'a' y el valor debe ser el número ASCII (a -> 97, b -> 98, …).
Tips: se puede utilizar la función chr para convertir un número en su correspondiente letra o ord para la
situación inversa (conocer el valor ASCII de una letra). También recordar que se puede crear un diccionario vacío
con dict().

Resultado Esperado:
{'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h':
104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111,
'p': 112, 'q': 113, 'r': 114, 's': 115
"""

def abecedario_ascii(inicio="a", final="z"):
    if ord(inicio) < 97 or ord(final) > 122:
        print("NO LOCO NO")
        return
    ascii = ord(inicio)
    letra = chr(ascii)
    while letra != "z":
        print(f"Letra: {chr(ascii)}, ascii: {ascii}")
        letra = chr(ascii)
        ascii += 1

inicio = "a"
final = "z"
abecedario_ascii(inicio, final)

