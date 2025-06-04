"""
5. Escriba una función que reciba como parámetro el radio de un circulo y devuelva una tupla conteniendo 
en el primer elemento el perímetro y en el segundo el área del mismo.  
TIPs: Recuerde que la fórmula del perímetro es (2 * pi * r) y el área se define como (pi * r^2). Se puede 
utilizar la constante pi definida en el módulo math (import math) 
Resultado Esperado: Si se utiliza la funcion con el valor de r=5, entonces debe devolver la tupla (31.415, 
78.539)
"""
import math

def funcion_radio(radio):
    """Devuelve un tupla con el perimetro y el area del radio ingresado como parametro"""
    perimetro = round(2 * math.pi * radio,3)
    area = round(math.pi * (radio ** 2),4)
    tupla=(perimetro,area)

    return tupla

radio=5
print(funcion_radio(radio))