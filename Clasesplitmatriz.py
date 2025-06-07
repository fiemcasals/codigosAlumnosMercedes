# Clase para dividir cadenas identificando un separador especifico, estas cadenas se almacenan en una lista que a su vez, mientras yo siga ingresando cadenas y sepadores, cada cadena ya separada se va almacenando en una matriz. Luego que ya terminé de ingresar las cadenas se imprime la matriz resultante.
class splitador:
    def __init__(self):
        pass
    def split(self, cadena, separador):
        # Dividir la cadena usando el separador
        return cadena.split(separador)
    def matriz(self, cadenas, separador):
        # Crear una matriz para almacenar las cadenas divididas
        matriz = []
        for cadena in cadenas:
            # Dividir cada cadena y agregarla a la matriz
            matriz.append(self.split(cadena, separador))
        return matriz
    def imprimir_matriz(self, matriz):
        # Imprimir la matriz resultante
        for fila in matriz:
            print(fila)
# Ejemplo de uso
if __name__ == "__main__":
    splitador_obj = splitador()
    cadenas = []
    while True:
        cadena = input("Ingrese una cadena (o 'salir' para terminar): ")
        if cadena.lower() == 'salir':
            break
        separador = input("Ingrese el separador: ")
        cadenas.append(cadena)
    matriz_resultante = splitador_obj.matriz(cadenas, separador)
    print("Matriz resultante:")
    splitador_obj.imprimir_matriz(matriz_resultante)
