# Clase para dividir cadenas identificando un separador especifico, estas cadenas se almacenan en una lista que a su vez se van almacenando en una matriz. luego se imprime la matriz resultante.
class splitador:
    def __init__(self):
        pass

    def splitter(self, cadena, seprador):
        split = cadena.split(seprador)
        return split
    def ejecutar(self):
        while True:
            print("\n--- Split Separador ---")
            cadena = input("Ingrese la cadena a separar: ")
            separador = input("Ingrese el separador: ")

            resultado = self.splitter(cadena, separador)
            print("\n--- Resultado ---")
            for i, item in enumerate(resultado):
                print(f"Elemento {i + 1}: {item}")
            print("\n--- Matriz ---")
            matriz = [resultado]
            for fila in matriz:
                print(fila)
            continuar = input("\n¿Desea continuar? (s/n): ").strip().lower()
            if continuar != 's':
                print("Saliendo del programa.")
                break
if __name__ == "__main__":
    splitador = splitador()
    splitador.ejecutar()