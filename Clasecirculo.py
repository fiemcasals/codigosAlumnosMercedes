# clase que recibe un radio y calcula el area y el perimetro de un circulo, imprimiendo los resultados en pantalla.
import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    def imprimir_resultados(self):
        print(f"Radio: {self.radio}")
        print(f"Área: {self.area()}")
        print(f"Perímetro: {self.perimetro()}")
# Ejemplo de uso
if __name__ == "__main__":
    radio = float(input("Ingresa el radio del círculo: "))
    circulo = Circulo(radio)
    circulo.imprimir_resultados()