# clase que recibe un radio, calcula el area y el perimetro de un circulo, imprimiendo los resultados en pantalla, limitado a 2 decimales.
import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return round(math.pi * (self.radio ** 2), 2)

    def perimetro(self):
        return round(2 * math.pi * self.radio, 2)

    def imprimir_resultados(self):
        print(f"Radio: {self.radio:.2f}")
        print(f"Area: {self.area():.2f}")
        print(f"Perimetro: {self.perimetro():.2f}")
# Ejemplo de uso
if __name__ == "__main__":
    radio = float(input("Ingresa el radio del círculo: "))
    circulo = Circulo(radio)
    circulo.imprimir_resultados()