#3 Escribir una funcion que genere y retorne un diccionario ASCII.
#  La funcion debe recibir como argumento el abecedario en minusculas y mayusculas. 
#  Para ello las claves deben ser las letras del abecedario y los valores deben ser el valor ASCII de cada letra.
#  Por ejemplo, la letra 'a' tendra como valor 97, la letra 'b' tendra como valor 98, etc.

def diccionario_ascii(abc):
  diccionario={}
  if abc.islower() == True:
    contador = 97
  else:
    contador = 65
  
  for pos in abc:
    diccionario.update({f"{pos}":contador})
    contador += 1
    
  for clave in diccionario.keys():
    print(f"Clave: {clave}    Valor: {diccionario[clave]}")

def diccionario_ascii2(abc):
  diccionario={}
  
  for pos in abc:
    diccionario.update({f"{pos}":ord(pos)})
  for clave in diccionario.keys():
    print(f"Clave: {clave}    Valor: {diccionario[clave]}")

########## Fin de funciones ########## 

abecedarioMin="abcdefghijklmnopqrstuvwxyz"
abecedarioMay = abecedarioMin.swapcase()

print("Diccionario ASCII minusculas:")
diccionario_ascii(abecedarioMin)
print(" ")
print("Diccionario ASCII mayusculas:")
diccionario_ascii(abecedarioMay)
print(" ")
print("Diccionario ASCII Version 2:")
diccionario_ascii2(abecedarioMin)
print(" ")
diccionario_ascii2(abecedarioMay)


