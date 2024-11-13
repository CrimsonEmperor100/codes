# Function to print the Sudoku board
def print_board(board):
    for row in board:
        print(" ".join(str(x) if x != 0 else '.' for x in row))

# Function to check if placing num at position (row, col) is valid
def is_safe(board, row, col, num):
    # Check if num is not in the same row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check if num is not in the same column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check if num is not in the same 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

# Function to solve the Sudoku puzzle using backtracking
def solve_sudoku(board):
    empty_cell = find_empty_location(board)
    if not empty_cell:  # No more empty cells, puzzle solved
        return True

    row, col = empty_cell

    for num in range(1, 10):  # Try numbers 1 to 9
        if is_safe(board, row, col, num):
            board[row][col] = num  # Place num

            if solve_sudoku(board):  # Recur to place the rest of the numbers
                return True

            board[row][col] = 0  # Backtrack if num doesn't lead to a solution

    return False  # Trigger backtracking if no number can be placed in this cell

# Helper function to find an empty location in the Sudoku board
def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  # 0 represents an empty cell
                return i, j
    return None  # No empty cell found

# Function to accept user input for the Sudoku board
def input_sudoku():
    print("Enter the 9x9 Sudoku puzzle row by row (use 0 for empty cells):")
    board = []
    for i in range(9):
        while True:
            try:
                row = list(map(int, input(f"Row {i + 1} (9 numbers separated by spaces): ").strip().split()))
                if len(row) == 9 and all(0 <= x <= 9 for x in row):
                    board.append(row)
                    break
                else:
                    print("Each row must have exactly 9 numbers between 0 and 9. Try again.")
            except ValueError:
                print("Invalid input. Please enter 9 integers separated by spaces.")
    return board

# Main function
def main():
    board = input_sudoku()
    print("\nOriginal Sudoku Board:")
    print_board(board)

    if solve_sudoku(board):
        print("\nSudoku solved successfully!")
        print_board(board)
    else:
        print("\nNo solution exists.")

# Run the program
if __name__ == "__main__":
    main()
#Enter the 9x9 Sudoku puzzle row by row (use 0 for empty cells):
#Row 1 (9 numbers separated by spaces): 1 0 0 1 0 0 2 0 0
#Row2 (9 numbers separated by spaces): 3 0 0 8 0 0 1 0 5
#Row 3 (9 numbers separated by spaces): 0 4 2 0 3 8 0 0 1
#Row 4 (9 numbers separated by spaces): 0 0 2 0 4 0 2 0 0
#Row 5 (9 numbers separated by spaces): 1 0 0 0 0 6 0 9 0
#Row 6 (9 numbers separated by spaces): 2 0 1 0 5 6 0 8 7
#Row 7 (9 numbers separated by spaces): 2 5 0 4 3 8 0 2 0
#Row 8 (9 numbers separated by spaces): 8 0 2 0 1 6 3 8 0
#Row 9 (9 numbers separated by spaces): 1 2
#Each row must have exactly 9 numbers between 0 and 9. Try again.
#Row 9 (9 numbers separated by spaces): 1 0 4 0 5 9 6 0 0

#Original Sudoku Board:
#1 . . 1 . . 2 . .
#3 . . 8 . . 1 . 5
#. 4 2 . 3 8 . . 1
#. . 2 . 4 . 2 . .
#1 . . . . 6 . 9 .
#2 . 1 . 5 6 . 8 7
#2 5 . 4 3 8 . 2 .
#8 . 2 . 1 6 3 8 .
#1 . 4 . 5 9 6 . .

#No solution exists.

