class Calculadora:
    def __init__(self):
        pass

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Error: División por cero"
        return a / b

    def ejecutar(self):
        while True:
            print("\n--- Calculadora ---")
            try:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                operacion = input("Ingrese la operación (+, -, *, /): ")

                if operacion == "+":
                    resultado = self.sumar(a, b)
                elif operacion == "-":
                    resultado = self.restar(a, b)
                elif operacion == "*":
                    resultado = self.multiplicar(a, b)
                elif operacion == "/":
                    resultado = self.dividir(a, b)
                else:
                    print("Operación no válida.")
                    continue

                print(f"El resultado es: {resultado}")
            except ValueError:
                print("Por favor, ingrese números válidos.")
                continue

            seguir = input("¿Hacer otra operación? (s/n): ").lower()
            if seguir != "s":
                break

if __name__ == "__main__":
    calc = Calculadora()
    calc.ejecutar()