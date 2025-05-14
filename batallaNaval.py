import random
import string

# Configuración inicial
LETTERS = list("ABCDE")
NUMBERS = list(range(1, 6))
BOARD_SIZE = 5
SHIP_COUNT = 3

# Crear un tablero vacío
def create_board():
    return [["~" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Imprimir el tablero
def print_board(board, show_ships=False):
    print("  " + " ".join(LETTERS))
    for i, row in enumerate(board):
        display_row = [cell if show_ships or cell != "S" else "~" for cell in row]
        print(f"{i+1} {' '.join(display_row)}")

# Convertir coordenadas 'A1' a índices [0][0]
def parse_coords(coord):
    try:
        x = LETTERS.index(coord[0].upper())
        y = int(coord[1]) - 1
        if x in range(5) and y in range(5):
            return y, x
    except:
        pass
    return None

# Colocar naves aleatorias
def place_ships_randomly(board, count):
    placed = 0
    while placed < count:
        x = random.choice(LETTERS)
        y = random.choice(NUMBERS)
        coord = parse_coords(f"{x}{y}")
        if coord and board[coord[0]][coord[1]] == "~":
            board[coord[0]][coord[1]] = "S"
            placed += 1

# Verificar si todas las naves fueron hundidas
def all_ships_sunk(board):
    for row in board:
        if "S" in row:
            return False
    return True

# Juego principal
def play_game():
    player_board = create_board()
    computer_board = create_board()

    place_ships_randomly(player_board, SHIP_COUNT)
    place_ships_randomly(computer_board, SHIP_COUNT)

    print("¡Bienvenido a Batalla Naval!")
    
    while True:
        print("\nTu tablero:")
        print_board(player_board, show_ships=True)
        
        print("\nTablero enemigo:")
        print_board(computer_board, show_ships=False)

        # Turno del jugador
        player_input = input("\nDispará (ej: A3): ").strip().upper()
        target = parse_coords(player_input)
        if not target:
            print("Coordenadas inválidas. Probá de nuevo.")
            continue

        row, col = target
        if computer_board[row][col] in ("X", "O"):
            print("Ya disparaste ahí. Probá otro.")
            continue

        if computer_board[row][col] == "S":
            print("¡Tocado!")
            computer_board[row][col] = "X"
        else:
            print("Agua.")
            computer_board[row][col] = "O"

        if all_ships_sunk(computer_board):
            print("\n¡Ganaste! Hundiste todas las naves enemigas.")
            break

    

        # Turno de la computadora
        while True:
            enemy_row = random.randint(0, 4)
            enemy_col = random.randint(0, 4)
            if player_board[enemy_row][enemy_col] not in ("X", "O"):
                break

        if player_board[enemy_row][enemy_col] == "S":
            print(f"La computadora te pegó en {LETTERS[enemy_col]}{enemy_row+1}!")
            player_board[enemy_row][enemy_col] = "X"
        else:
            print(f"La computadora tiró en {LETTERS[enemy_col]}{enemy_row+1} y fue agua.")
            player_board[enemy_row][enemy_col] = "O"

        if all_ships_sunk(player_board):
            print("\n¡Perdiste! Te hundieron todas las naves.")
            break

if __name__ == "__main__":
    play_game()
