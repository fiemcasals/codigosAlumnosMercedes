def imprimir_numeros_especiales(inicio, fin):
    resultado = []

    for i in range(inicio, fin + 1):
        if i % 7 == 0 and i % 5 != 0:
            print(i)
            resultado.append(str(i))

    print(','.join(resultado))
    return resultado  


def pedir_rango_y_mostrar():
    try:
        inicio = int(input("Ingrese el numero de inicio (entre 1 y 100): "))
        fin = int(input("Ingrese el numero de fin (entre 1 y 100): "))

        if 1 <= inicio <= 100 and 1 <= fin <= 100:
            if inicio <= fin:
                imprimir_numeros_especiales(inicio, fin)
            else:
                print("El numero de inicio debe ser menor o igual al numero de fin.")
        else:
            print("Ambos numeros deben estar entre 1 y 100.")
    except ValueError:
        print("Por favor, ingrese numeros enteros validos.")



pedir_rango_y_mostrar()
