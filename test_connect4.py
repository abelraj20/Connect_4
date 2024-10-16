import numpy as np

# This creates a new 2D array (6x7) that shows the board. 
# It sets all spaces to 0, showing there is no piece in that location.
def create_board():
    board = np.zeros((6,7))
    return board

# This drops the piece into the given row and column on the board. 
# It updates the corresponding element in the 2D array to the specified piece value (either 1 or 2).
def piece_dropped(board, row, col, piece):
    board[row][col] = piece

# This checks if the given column on the board is a clear location to drop a piece. 
# Returns True if the bottom row is empty (value of 0) and False if not.
def clear_location(board, col):
    return board[5][col] == 0

# This finds the next available row in a given column where a piece can be dropped. 
# Searches from the top of the column downwards and gives the row number of the first empty slot.
def next_open_row(board, col):
    for r in range(6):
        if board[r][col] == 0:
            return r

# This prints the game board to the terminal. The flip() function to reverses the order of the rows.
# So, the bottom row is printed first and the top row is printed last.
def print_board(board):
    print(np.flip(board, 0))

# Checks if the particular player has won the game. 
# It checks for four pieces in a row (horizontally, vertically, or diagonally).
# It starts from every possible location. If it finds a winning combination, it returns True.
def winning_move(board, piece):
    # Horizontal locations are checked.
    for c in range(4):
        for r in range(6):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Vertical locations are checked.
    for c in range(7):
        for r in range(3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Diagonals which are sloped upwards are checked.
    for c in range(4):
        for r in range(3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    # Diagonals which are sloped downwards are checked.
    for c in range(4):
        for r in range(3, 6):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
# This creates the board as the game is not over.
def main():
    board = create_board()
    game_over = False
    turn = 0

# During the game, the first player (1) is asked to play a turn.
# 0 is the first column and 6 is the last column.
    while not game_over:
        if turn == 0:
            col = int(input("Player 1 make your selection (0-6):"))

            if clear_location(board, col):
                row = next_open_row(board, col)
                piece_dropped(board, row, col, 1)
                # If the move is a winning move, the first player is congratulated.
                if winning_move(board, 1):
                    print("Player 1 Wins!!! Congratulations!")
                    game_over = True
        # The second player (2) is asked to play a turn.
        else:
            col = int(input("Player 2 make your selection (0-6):"))

            if clear_location(board, col):
                row = next_open_row(board, col)
                piece_dropped(board, row, col, 2)
                # If the move is a winning move, the second player is congratulated.
                if winning_move(board, 2):
                    print("Player 2 Wins!!! Congratulations!")
                    game_over = True

        print_board(board)
        turn += 1
        turn = turn % 2
    # If a specified player has won, the game is determined to be over.
    print("Game Over!")

if __name__ == '__main__':
    main()