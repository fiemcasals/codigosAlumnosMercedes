"""
9. Se necesita un programa que reciba por parámetro un texto, y que devuelva una tupla conteniendo en el 
primer lugar, la cantidad de letras (mayúsculas o minúsculas), en el segundo lugar la cantidad de dígitos 
numéricos y en el tercer lugar, otros símbolos.  
Resultado Esperado (tupla): Por ejemplo, si se utiliza como parámetro el texto: "Esta es una 
mañana LLuviosa!! 25 días más serán así??" se debería obtener como resultado la tupla  
(38, 2, 13) 
TIPs: Python cuenta con las funciones isdigit() y isalpha() utilizadas sobre strings (o "chars") que pueden ser útiles 
para identificar tipos de caracteres. Por ejemplo, '9'.isdigit() retorna True y '!'.isalpha() retorna 
False. Buscar en la documentación mayor detalle.
"""

def funcion_cuenta_tupla(texto):
  cant_letras=0
  cant_num=0
  cant_simbol=0
  
  for dato in texto:
    if dato.isalpha():
      cant_letras += 1
    elif dato.isdigit():
      cant_num += 1
    else:
      cant_simbol += 1
  tupla = (cant_letras,cant_num,cant_simbol)
  return tupla
  
txt = "Esta es una mañana LLuviosa!! 25 días más serán así??"
print(funcion_cuenta_tupla(txt))

