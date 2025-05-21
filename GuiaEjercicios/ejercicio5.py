# Escriba una función que reciba como parámetro el radio de un circulo y devuelva una tupla conteniendo en el primer elemento el perímetro y en el segundo el área del mismo.
# TIPs: Recuerde que la fórmula del perímetro es (2 * pi * r) y el área se define como (pi * r^2). Se puede utilizar la constante pi definida en el módulo math (import math)
# Resultado Esperado:Si se utiliza la funcion con el valor de r=5, entonces debe devolver la tupla (31.415, 78.539)

import math

def calcular_perimetro_y_area(radio):
    perimetro = 2 * math.pi * radio
    area = math.pi * radio ** 2
    return (perimetro, area) #devuelvo una tupla con el perímetro y el área

# Ejemplo de uso
radio = 5
perimetro, area = calcular_perimetro_y_area(radio) # desempaqueto la tupla, así puedo usar los valores por separado
print(f"Perímetro: {perimetro}, Área: {area}")