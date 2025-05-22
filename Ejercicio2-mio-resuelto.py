# Escribir una funcion factorial que reciba como parametro un numero inicial y compute su resultado
# a) El factorial de 8: 8*7*6*5*4*3*2*1=40320.Recuerde que el factorial de 0 es 1.
# b) Hacer la implementacion inversa (si lo hizo recursivamente, implemente la iterativa y viceversa).

def factorial_iterativo(fac):
  resultado = fac
  for num in range(fac,1,-1):
    if fac != 0:
      if num != 1:
        resultado = resultado*(num-1)
    else:
      resultado = 1
  print(f"El factorial de {fac} es:",resultado)

def factorial_recursivo(fac):
  if fac == 0:
    return 1
  else:
    return fac * factorial_recursivo(fac-1)
  
factorial = int(input("Ingrese un numero para saber su factorial...."))
# a) Iterativa
factorial_iterativo(factorial)
print(" ")
# b) Recursiva 
print("Mismo factorial con funcion recursiva:")
print(factorial_recursivo(factorial))