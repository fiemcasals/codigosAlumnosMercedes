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

def main():
    calc = Calculadora()
    while True:
        print("\n--- Calculadora ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        opcion = input("Elija una opción (1-5): ")
        if opcion == "5":
            print("¡Hasta luego!")
            break
        if opcion not in ("1", "2", "3", "4"):
            print("Opción no válida. Intente de nuevo.")
            continue
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Por favor, ingrese números válidos.")
            continue
        if opcion == "1":
            resultado = calc.sumar(a, b)
        elif opcion == "2":
            resultado = calc.restar(a, b)
        elif opcion == "3":
            resultado = calc.multiplicar(a, b)
        elif opcion == "4":
            resultado = calc.dividir(a, b)
        print(f"El resultado es: {resultado}")

if __name__ == "__main__":
    main()