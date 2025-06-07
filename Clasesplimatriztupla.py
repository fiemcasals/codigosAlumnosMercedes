# Clase para dividir cadenas identificando un separador especifico independiente para cada cadena (se envia a la clase como una tupla), estas cadenas se almacenan en una lista que a su vez, mientras yo siga ingresando cadenas y sepadores, cada cadena ya separada se va almacenando en una matriz. Luego que ya terminé de ingresar las cadenas se imprime la matriz resultante.
class splitador:
    def __init__(self):
        pass

    def split(self, cadena, separador):
        # Dividir la cadena usando el separador
        return cadena.split(separador)

    def matriz(self, cadenas, separadores):
        # Crear una matriz para almacenar las cadenas divididas
        matriz = []
        for i in range(len(cadenas)):
            # Dividir cada cadena con su respectivo separador y agregarla a la matriz
            matriz.append(self.split(cadenas[i], separadores[i]))
        return matriz

    def imprimir_matriz(self, matriz):
        # Imprimir la matriz resultante
        for fila in matriz:
            print(fila)
# Ejemplo de uso
if __name__ == "__main__":
    splitador_obj = splitador()
    cadenas = []
    separadores = []
    while True:
        cadena = input("Ingresa una cadena (o 'salir' para terminar y mostrar la matriz resultante): ")
        if cadena.lower() == 'salir':
            break
        separador = input("Ingresa el separador: ")
        cadenas.append(cadena)
        separadores.append(separador)
    matriz_resultante = splitador_obj.matriz(cadenas, separadores)
    print("Matriz resultante:")
    splitador_obj.imprimir_matriz(matriz_resultante)