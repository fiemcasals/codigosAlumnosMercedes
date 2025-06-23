# Juego TA-TE-TI implementado como una clase en Python, dos jugadores X y O, e implementado como un vector de 9 elementos, si un jugador selecciona una posición ya ocupada, pierde su turno, el juego termina cuando un jugador gana o hay empate, se debe mostrar el tablero en cada jugada y al final del juego.
class TaTeTi:
    def __init__(self):
        self.tablero = [" " for _ in range(9)]
        self.jugador_actual = "X"

    def imprimir_tablero(self):
        print("\n")
        for i in range(3):
            print(" | ".join(self.tablero[i*3:(i+1)*3]))
            if i < 2:
                print("-" * 9)
        print("\n")

    def verificar_ganador(self):
        combinaciones_ganadoras = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Filas
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columnas
            (0, 4, 8), (2, 4, 6)              # Diagonales
        ]
        for a, b, c in combinaciones_ganadoras:
            if self.tablero[a] == self.tablero[b] == self.tablero[c] != " ":
                return True
        return False

    def tablero_lleno(self):
        return all(celda != " " for celda in self.tablero)

    def jugar(self):
        while True:
            self.imprimir_tablero()
            print(f"Turno del jugador {self.jugador_actual}")
            try:
                posicion = int(input("Elegí una posición (0-8): "))
            except ValueError:
                print("Por favor, ingresá un número válido.")
                continue

            if 0 <= posicion < 9:
                if self.tablero[posicion] == " ":
                    self.tablero[posicion] = self.jugador_actual
                    if self.verificar_ganador():
                        self.imprimir_tablero()
                        print(f"¡El jugador {self.jugador_actual} ganó!")
                        break
                    elif self.tablero_lleno():
                        self.imprimir_tablero()
                        print("¡Empate!")
                        break
                    self.jugador_actual = "O" if self.jugador_actual == "X" else "X"
                else:
                    print("¡Esa posición ya está ocupada!")
            else:
                print("Posición inválida. Usá números del 0 al 8.")
if __name__ == "__main__":
    juego = TaTeTi()
    juego.jugar()
# Este código implementa un juego de Ta-Te-Ti (Tic-Tac-Toe) en Python.
