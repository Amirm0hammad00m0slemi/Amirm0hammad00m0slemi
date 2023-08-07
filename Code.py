import random

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = random.choice(players)

    while True:
        print_board(board)
        print("Player", current_player, "turn")

        if current_player == "X":
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] != " ":
                print("Invalid move. Try again.")
                continue
            board[row][col] = "X"
        else:
            # Computer's turn (random move)
            while True:
                row = random.randint(0, 2)
                col = random.randint(0, 2)
                if board[row][col] == " ":
                    board[row][col] = "O"
                    break

        if check_winner(board, current_player):
            print_board(board)
            print("Player", current_player, "wins!")
            break
        elif all(board[row][col] != " " for row in range(3) for col in range(3)):
            print_board(board)
            print("It's a tie!")
            break

        current_player = players[(players.index(current_player) + 1) % 2]

play_game()
