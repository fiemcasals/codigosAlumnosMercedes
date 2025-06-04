"""
4. Escribir un programa que reciba como parámetro un string de elementos separados por coma y retorne 
una lista conteniendo cada elemento.  
Resultado Esperado: Si se utiliza como parámetro el string '14,Juana Perez,True' se espera 
que la función retorne la lista ['14', 'Juana Perez', 'True'] 
b. Modificar la función anterior, pero obteniendo correctamente cada dato según su tipo (numero entero, 
string o boolean). Se considera que el string siempre tiene la forma de primer campo un entero, luego un 
texto y por ultimo un boolean. 
Resultado Esperado: Si se envia '14,Juana Perez,True' se espera que la función retorne la 
lista [14, 'Juana Perez', True] 
c. 
Utilizando la función realizada en el punto 4b, hace una nueva función que reciba una  lista de strings y 
retorna otra lista, como listas con los campos formateados (mantener el mismo formato de string que el 
punto b, es decir, entero, texto y boolean).  
Resultado Esperado: Si se envía la siguiente lista como parámetro de la función: 
[  
'14,Juana Perez,True',  
'16,Raul Dell,False',  
'18,Mariana Castillo,True',  
'176,Pedro Rodríguez,False' 
] 
Se espera obtener la lista: 
[[14, 'Juana Perez', True], [16, 'Raul Dell', True], [18, 'Mariana Castillo', 
True], [176, 'Pedro Rodríguez', True]]
"""
#a
def funcion_a(string):
    """Recibe como parámetro un string de elementos 
    separados por coma y retorna 
    una lista conteniendo cada elemento."""
    lista=[]
    variable = ""
    for i in range(len(string)):
        if string[i] != ",":
           variable += string[i]
        if string[i] == "," or i == len(string) - 1:
           lista.append(variable)
           variable = ""
    return lista
    
print("Funcion A:" , funcion_a('14,Juana Perez,True'))

#b
def funcion_b(string):
    lista=[]
    variable = ""
    posicion = 1
    for i in range(len(string)):
        if string[i] != ",":
            variable += string[i]
        if string[i] == "," or i == len(string) - 1:
            if posicion == 1:
                lista.append(int(variable))
                print(lista[posicion-1],type(lista[posicion-1]))
                posicion += 1
            elif posicion == 2:
                lista.append(str(variable))
                print(lista[posicion-1],type(lista[posicion-1]))
                posicion += 1
            else:
                if variable == "False":
                    lista.append(bool(0))# 0 devuelve False
                else:
                    lista.append(bool(1))# 1 devuelve True
                print(lista[posicion-1],type(lista[posicion-1]))
            variable = ""

print()
print("Funcion B:")
funcion_b('14,Juana Perez,True')

#c
"""[  
'14,Juana Perez,True',  
'16,Raul Dell,False',  
'18,Mariana Castillo,True',  
'176,Pedro Rodríguez,False' 
] 
Se espera obtener la lista: 
[[14, 'Juana Perez', True], [16, 'Raul Dell', True], [18, 'Mariana Castillo', 
True], [176, 'Pedro Rodríguez', True]]
"""
def funcion_c(lista_string):
    lista=[]
    lista_de_listas=[]
    
    for i in range(len(lista_string)):

        string = lista_string[i]
        comodin=""

        posicion = 1
        for i in range(len(string)):
            if string[i] != ",":
                comodin += string[i]
            if string[i] == "," or i == len(string) - 1:
                if posicion == 1:
                    lista.append(int(comodin))
                    posicion += 1
                elif posicion == 2:
                    lista.append(str(comodin))
                    posicion += 1
                elif posicion == 3:
                    if comodin == "False":
                        lista.append(bool(0))# 0 devuelve False
                    else:
                        lista.append(bool(1))# 1 devuelve True
                comodin=""
                
        lista_de_listas.append(lista)        
        lista=[]        
    return lista_de_listas

    
print()   
print("Funcion C:",funcion_c([  
'14,Juana Perez,True',  
'16,Raul Dell,False',  
'18,Mariana Castillo,True',  
'176,Pedro Rodríguez,False' 
]))