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
            print(f"El resultado es: {resultado}")

            seguir = input("¿Hacer otra operación? (s/n): ").lower()
            if seguir != "s":
                break
if __name__ == "__main__":
    split = splitador()
    split.ejecutar()