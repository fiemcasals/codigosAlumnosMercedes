"""
Enunciados de los 4 ejercicios recursivos
1. 🔢 Suma de elementos de una lista
Enunciado:
Implementar una función recursiva que reciba una lista de números y devuelva la suma total de sus elementos.
No se permite el uso de funciones iterativas ni funciones auxiliares como sum().
Ejemplo esperado:
suma_lista([1, 2, 3, 4]) → 10

lo primero es el caso base

lista = [1,2,3,4]

def suma_lista(lista):
  if not lista:
    return 0
  else:
    return lista[0] + suma_lista(lista[1:])
  
  

print(suma_lista(lista))
  

2. 🧮 Contar elementos en una lista
Enunciado:
Definir una función recursiva que reciba una lista y devuelva la cantidad de elementos que contiene.
No se permite usar la función len() para contar elementos.
Ejemplo esperado:
contar_elementos([10, 20, 30, 40]) → 4

def contar_lista(lista):
  # Caso base
  
  if len(lista) == 1:  
    return 1
  
  # Caso recursivo
  else:  
     return 1 + contar_lista(lista[1:])


def contar_lista(lista):
    # Caso base: si la lista está vacía, retorna 0
    print("antes del if")
    if not lista:
        return 0
    # Caso recursivo: cuenta el primer elemento y sigue con el resto
    else:
        return 1 + contar_lista(lista[1:])

print()
print("func:",contar_lista([10, 20, 30, 40]))
print("func:",contar_lista([]))


3. 🔁 Invertir una lista

Enunciado:
Escribir una función recursiva que reciba una lista y retorne una nueva lista con los mismos elementos en orden inverso.
No se permite utilizar ciclos ni funciones como reversed().

Ejemplo esperado:
invertir_lista([1, 2, 3]) → [3, 2, 1]

lista=[1,2,3]

def dar_vuelta_lista(lista):
  if not lista:
    return lista
  else:
    print("Lista pos ult:",[lista[-1]])
    print("Lista:",lista)
    input()
    return [lista[-1]] + dar_vuelta_lista(lista[:-1])
    
    
   
  
print(dar_vuelta_lista(lista))









4. 🔤 Verificar si una palabra es palíndromo

Enunciado:
Crear una función recursiva que determine si una cadena de texto es un palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a izquierda).
No se permite invertir la cadena con slicing ni usar funciones auxiliares.

Ejemplos esperados:
es_palindromo("reconocer") → True
es_palindromo("hola") → False
"""


str="reconoer"

def es_palindromo(valor):
  print("principio")
  print(valor[0])
  print()
  print(valor[-1:])
  print("resto")
  print(valor[1:-1])
  print("ultimo del resto",valor[-1])

  
    
    
  if valor[1:-1] and valor[0] == valor[-1:]:
    input("Presiona enter, estoy en el elif")
    es_palindromo(valor[1:-1])
    return True
  elif valor[0] != valor[-1]:
    return False
    
    
   
  
print("func",es_palindromo(str))

