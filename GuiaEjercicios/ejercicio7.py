# Se necesita una función que reciba un texto de varias palabras separadas por un espacio, con letras mayúsculas y minúsculas, y retorne una colección las palabras utilizadas, todas en minúscula y sin duplicados
# Resultado Esperado: Si por ejemplo el programa solicitara ingresar el texto y el usuario ingresa:
# Por favor, ingrese un texto: HOLA NO Deberia deberia haber duplicados de de de de de ningun tipo
# Se debería obtener como resultado: {'haber', 'ningun', 'duplicados', 'deberia', 'tipo', 'no', 'de', 'hola'}

def procesar_texto(texto):
    # Divido el texto en palabras y las convierto a minúsculas, el resultado se guarda en una lista(palabras)
    palabras = texto.lower().split()
    
    # Uso una colección set para eliminar duplicados y guardo el resultado en palabras_unicas
    # set() crea una colección de elementos únicos, eliminando duplicados
    palabras_unicas = set(palabras)
    
    
    return palabras_unicas

#ejemplo de uso     

texto = input("Por favor, ingrese un texto: ")
resultado = procesar_texto(texto)
print(resultado)