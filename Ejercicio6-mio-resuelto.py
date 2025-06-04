"""
6. Se necesita un programa que reciba por línea de comando una serie de palabras, hasta que reciba la 
palabra "exit". Una vez recibida dicha instrucción, debe mostrar por salida standard las mismas palabras 
ingresadas, almacenadas en una lista, pero ordenadas alfabéticamente y cada una debe estar 
capitalizada.  
Resultado Esperado: El programa le solicita al usuario que ingrese y este escribe: 
Ingrese palabra: hola 
Ingrese palabra: QUE 
Ingrese palabra: tal 
Ingrese palabra: como
Ingrese palabra: estas 
Ingrese palabra: exit 
Se espera recibir el siguiente resultado: ['Como', 'Estas', 'Hola', 'Que', 'Tal'] 

"""

def ordena_palabras():
    opcion = ""
    lista_desordenada = []
    while opcion != "exit":
        opcion = input("Ingrese una palabra... para terminar ingrese 'exit'").lower()
        if opcion != "exit":
            lista_desordenada.append(opcion.capitalize())

    lista_ordenada = sorted(lista_desordenada)
    print(lista_ordenada)

ordena_palabras()