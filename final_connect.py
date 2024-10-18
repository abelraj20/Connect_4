import numpy as np

# Create a new 6x7 game board.
def create_board():
    board = np.zeros((6, 7))
    return board

# Drop the piece into the board.
def piece_dropped(board, row, col, piece):
    board[row][col] = piece

# Check if the column is clear for a piece to be dropped.
def clear_location(board, col):
    return board[5][col] == 0

# Find the next available row in a given column.
def next_open_row(board, col):
    for r in range(6):
        if board[r][col] == 0:
            return r

# Print the game board with proper formatting (without apostrophes).
def print_board(board):
    print("\n  1  2  3  4  5  6  7")  # Column numbers (1-7)
    visual_board = board_visual(board)
    for row in np.flip(visual_board, 0):  # Flip to display properly
        print("| " + "  ".join(row) + " |")  # Add side borders and align pieces

# Convert the board into a visual format with O, X, and . for readability.
def board_visual(board):
    visual = np.copy(board).astype(str)
    visual[board == 0] = "."
    visual[board == 1] = "O"
    visual[board == 2] = "X"
    return visual

# Check for a winning move (4 in a row).
def winning_move(board, piece):
    # Check horizontal locations for win.
    for c in range(4):
        for r in range(6):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win.
    for c in range(7):
        for r in range(3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals.
    for c in range(4):
        for r in range(3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals.
    for c in range(4):
        for r in range(3, 6):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

# Main function to run the game, including restart functionality.
def main():
    while True:
        board = create_board()
        game_over = False
        turn = 0  # Player 1 starts

        print_board(board)
        
        while not game_over:
            # Prompt Player 1 or Player 2 based on the turn.
            if turn == 0:
                col = int(input("\nPlayer 1 (O), make your selection (1-7): ")) - 1  # Adjust for 1-based indexing
                piece = 1
            else:
                col = int(input("\nPlayer 2 (X), make your selection (1-7): ")) - 1  # Adjust for 1-based indexing
                piece = 2
            
            # Check if the column is clear and drop the piece.
            if clear_location(board, col):
                row = next_open_row(board, col)
                piece_dropped(board, row, col, piece)
                
                # Check for a winning move.
                if winning_move(board, piece):
                    print_board(board)
                    print(f"\nPlayer {turn + 1} ({'O' if piece == 1 else 'X'}) Wins!!! Congratulations!")
                    game_over = True
            
            print_board(board)  # Print the updated board
            
            turn += 1
            turn = turn % 2  # Alternate between Player 1 and Player 2
        
        # Prompt the players if they want to restart the game.
        restart = input("\nGame Over! Do you want to play again? (yes/no): ").lower()
        if restart != "yes":
            print("Thanks for playing!")
            break  # Exit the game if the players choose not to restart

if __name__ == '__main__':
    main()