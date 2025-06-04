"""
8. En Años anteriores, se necesitaba una función en python que reciba un texto conteniendo bits (simbolos 
1 y 0), y debia armar una lista conteniendo 8 bits por elementos (1 byte). Por ejemplo, si se incova la 
funcion con el siguiente texto como parámetro:  
"1001010101000101010101100101001010101010"  
la funcion devuelve: ['10010101', '01000101', '01010110', '01010010', 
'10101010'] 
El programador de ese momento armó el siguiente código: 
def ej08a(texto): 
Arma una lista de bytes acorde al texto recibido por parametro
indice = 0 
resultado = [] 
current_byte = "" 
for i in texto: 
current_byte += i  # se agrega el nuevo caracter al byte actual 
indice += 1  # se incrementa en uno el indice 
if indice % 8 == 0:   
# Comienza un nuevo byte 
resultado.append(str(current_byte))  
current_byte = "" 
return resultado 
que funciona según lo estipulado (probarlo para entenderlo). Se pide que analice el código y que conteste lo 
siguiente: 
a. ¿Qué cambios agregaría a la función para verificar que el texto ingresado solo contiene caracteres “1” o 
“0” antes de ser procesado? 
b. ¿Qué objetivo tiene la validacion indice % 8 == 0? 
c. 
¿En la línea 13, porque usa la función str si current_byte ya es un string? 
d. ¿Existe alguna manera rápida y sencilla si se pide modificar la función para que la lista resultado no 
contenga duplicados? En caso de existir, explique cuál sería.
"""