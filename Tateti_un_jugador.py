# Juego TA-TE-TI implementado como una clase en Python, un jugador es X el otro es la computadora O, e implementado como un vector de 9 elementos, si el jugador selecciona una posición ya ocupada, pierde su turno, el juego termina cuando un jugador gana o hay empate, se debe mostrar el tablero en cada jugada y al final del juego.
import random

class TatetiUnJugador:
    def __init__(self):
        self.tablero = [" " for _ in range(9)]
        self.jugador = "X"
        self.computadora = "O"

    def mostrar_tablero(self):
        print("\nTablero:")
        for i in range(3):
            print("|".join(self.tablero[i*3:(i+1)*3]))
            if i < 2:
                print("-" * 5)

    def jugar(self, posicion):
        if self.tablero[posicion] == " ":
            self.tablero[posicion] = self.jugador
            if self.verificar_ganador(self.jugador):
                self.mostrar_tablero()
                print("¡Jugador X gana!")
                return True
            elif " " not in self.tablero:
                self.mostrar_tablero()
                print("¡Empate!")
                return True
            else:
                return False
        else:
            print("Posición ya ocupada. Pierdes tu turno.")
            return False

    def jugar_computadora(self):
        posiciones_libres = [i for i, x in enumerate(self.tablero) if x == " "]
        if posiciones_libres:
            posicion = random.choice(posiciones_libres)
            self.tablero[posicion] = self.computadora
            if self.verificar_ganador(self.computadora):
                self.mostrar_tablero()
                print("¡Computadora O gana!")
                return True
        return False

    def verificar_ganador(self, jugador):
        combinaciones_ganadoras = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Filas
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columnas
            (0, 4, 8), (2, 4, 6)              # Diagonales
        ]
        for a, b, c in combinaciones_ganadoras:
            if self.tablero[a] == self.tablero[b] == self.tablero[c] == jugador:
                return True
        return False

    def ejecutar(self):
        while True:
            self.mostrar_tablero()
            try:
                posicion = int(input("Jugador X, elige una posición (0-8): "))
                if self.jugar(posicion):
                    break
                if self.jugar_computadora():
                    break
            except ValueError:
                print("Entrada inválida. Por favor, elige un número entre 0 y 8.")
            except IndexError:
                print("Posición fuera de rango. Por favor, elige un número entre 0 y 8.")
        print("Juego terminado.")
if __name__ == "__main__":
    juego = TatetiUnJugador()
    juego.ejecutar()
    