
#1-Escribe una funcion que reciba como parametro el inicio y el fin (inclusive) de un rango numerico.

#La funcion debe:
#a) Imprimir en pantalla todos aquellos numeros que sean divisibles por 7 pero no por 5.
#b) Imprimir el mismo resultado anterior pero separado por comas.
#Ejemplo:
#Si el rango es 1-100, la salida debe ser:
#a)7
# 14
# 21
# 28...
#b)7,14,21,28,42,49,56,63,70,77,84,91,98

def divisibles1(inicio,fin):
  for num in range(inicio,fin):
    if num % 7 == 0 and num % 5 != 0:
      print(num)
  
def divisibles2(inicio,fin):
  resultado = []
  for num in range(inicio,fin):
    if num % 7 == 0 and num % 5 != 0:
      resultado.append(num)
  
  return resultado
  
def divisibles3(inicio,fin):
  resultado_var = []
  for num in range(inicio,fin):
    if num % 7 == 0 and num % 5 != 0:
      ddd = str(num)
      resultado_var.append(ddd)
  return ",".join(resultado_var)
    
print("Numeros divisibles por 7 y no por 5:")
divisibles1(1,100)
print(" ")

print("Lista divisibles retornando una lista:")
print(divisibles2(1,100))
print(" ")

print("Lista de divisibles retornando un string \nseparado por '','' :")
string=divisibles3(1,100)
print(string)
print(type(string))