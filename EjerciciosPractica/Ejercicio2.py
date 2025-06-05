#Escribir la función factorial, que reciba como parámetro el numero inicial y compute su resultado.  
#a. Ejemplo factorial(8) = 8*7*6*5*4*3*2*1 = 40320. Recuerde que factorial de 0 por definición es 1.  
#b. Hacer la implementación inversa (si lo hizo recursivo, hacerlo iterativo o viceversa)

#///////////RECURSIVA//////////
def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)
print(factorial_recursivo(8))  # Resultado: 40320

#/////////////ITERATIVA/////////////
def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
print(factorial_iterativo(8))  # Resultado: 40320

