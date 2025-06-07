# clase que recibe un radio, calcula el area, el diametro y el perimetro de un circulo, imprimiendo los resultados en pantalla, limitado a 2 decimales.
import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return round(math.pi * (self.radio ** 2), 2)

    def diametro(self):
        return round(2 * self.radio, 2)

    def perimetro(self):
        return round(2 * math.pi * self.radio, 2)

    def imprimir_resultados(self):
        print(f"Radio: {self.radio}")
        print(f"Area: {self.area()}")
        print(f"Diametro: {self.diametro()}")
        print(f"Perimetro: {self.perimetro()}")
# Ejemplo de uso
if __name__ == "__main__":
    radio = float(input("Ingresa el radio del círculo: "))
    circulo = Circulo(radio)
    circulo.imprimir_resultados()