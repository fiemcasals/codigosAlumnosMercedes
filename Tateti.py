# Juego TA-TE-TI implementado como una clase en Python, dos jugadores X y O, e implementado como un vector de 9 elementos, si un jugador selecciona una posición ya ocupada, pierde su turno, el juego termina cuando un jugador gana o hay empate, se debe mostrar el tablero en cada jugada y al final del juego.
class Tateti:
    def __init__(self):
        self.tablero = [" " for _ in range(9)]
        self.jugador_actual = "X"

    def mostrar_tablero(self):
        print("\nTablero:")
        for i in range(3):
            print("|".join(self.tablero[i*3:(i+1)*3]))
            if i < 2:
                print("-" * 5)

    def jugar(self, posicion):
        if self.tablero[posicion] == " ":
            self.tablero[posicion] = self.jugador_actual
            if self.verificar_ganador():
                self.mostrar_tablero()
                print(f"¡Jugador {self.jugador_actual} gana!")
                return True
            elif " " not in self.tablero:
                self.mostrar_tablero()
                print("¡Empate!")
                return True
            else:
                self.jugador_actual = "O" if self.jugador_actual == "X" else "X"
        else:
            print("Posición ya ocupada. Pierdes tu turno.")
        return False

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

    def ejecutar(self):
        while True:
            self.mostrar_tablero()
            try:
                posicion = int(input(f"Jugador {self.jugador_actual}, elige una posición (0-8): "))
                if posicion < 0 or posicion > 8:
                    print("Posición inválida. Debe ser un número entre 0 y 8.")
                    continue
            except ValueError:
                print("Entrada inválida. Debe ser un número.")
                continue

            if self.jugar(posicion):
                break
        print("Juego terminado.")
if __name__ == "__main__":
    juego = Tateti()
    juego.ejecutar()
    
