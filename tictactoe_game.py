import numpy as np

def print_board(board):
    """Print the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """Check if there is a winner."""
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0, col] == board[1, col] == board[2, col] and board[0, col] != " ":
            return board[0, col]

    if board[0, 0] == board[1, 1] == board[2, 2] and board[0, 0] != " ":
        return board[0, 0]

    if board[0, 2] == board[1, 1] == board[2, 0] and board[0, 2] != " ":
        return board[0, 2]

    return None


def is_full(board):
    """Check if the board is full."""
    return not np.any(board == " ")


def play_game():
    """Main function to play Tic Tac Toe."""
    board = np.full((3, 3), " ")
    current_player = "X"

    while True:
        print_board(board)

        try:
            user_move = input(f"Player {current_player}, enter your move as x,y coordinates (e.g., 1,2): ")
            x, y = map(int, user_move.split(","))
            x, y = x - 1, y - 1  # Adjust for 0-based indexing

            if board[x, y] != " ":
                print("Cell already taken. Choose another.")
                continue

            board[x, y] = current_player

            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break

            if is_full(board):
                print_board(board)
                print("It's a tie!")
                break

            current_player = "O" if current_player == "X" else "X"
        except (ValueError, IndexError):
            print("Invalid input. Please enter coordinates in the format x,y where x and y are between 1 and 3.")


if __name__ == "__main__":
    play_game()
