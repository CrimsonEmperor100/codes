# Function to print the solution
def printSol(board):
    for row in board:
        print(" ".join(str(x) for x in row))

# Function to check if a queen can be placed on board[row][col]
def isSafe(row, col, board, rowLookup, slashLookup, backslashLookup, N):
    if rowLookup[row] or slashLookup[row + col] or backslashLookup[row - col + N - 1]:
        return False
    return True

# Utility function to solve the N-Queens problem recursively
def solveNQUtil(board, col, rowLookup, slashLookup, backslashLookup, N):
    # Base case: If all queens are placed, return True
    if col >= N:
        return True

    # Try placing a queen in each row of the current column
    for i in range(N):
        if isSafe(i, col, board, rowLookup, slashLookup, backslashLookup, N):
            # Place the queen
            board[i][col] = 1
            rowLookup[i] = slashLookup[i + col] = backslashLookup[i - col + N - 1] = True

            # Recur to place the rest of the queens
            if solveNQUtil(board, col + 1, rowLookup, slashLookup, backslashLookup, N):
                return True

            # Backtrack: Remove the queen and reset flags
            board[i][col] = 0
            rowLookup[i] = slashLookup[i + col] = backslashLookup[i - col + N - 1] = False

    # If the queen cannot be placed in any row, return False
    return False

# Function to solve the N-Queens problem
def solveNQ():
    try:
        N = int(input("Enter the size of the board (N): "))
        if N <= 0:
            print("Please enter a positive integer greater than 0.")
            return solveNQ()

        # Initialize the chessboard
        board = [[0] * N for _ in range(N)]

        # Initialize lookup arrays for rows, slash diagonals, and backslash diagonals
        rowLookup = [False] * N
        slashLookup = [False] * (2 * N - 1)
        backslashLookup = [False] * (2 * N - 1)

        # Start solving from the first column
        if not solveNQUtil(board, 0, rowLookup, slashLookup, backslashLookup, N):
            print("Solution does not exist")
            return False

        # Print the solution
        print("\nSolution for N =", N)
        printSol(board)
        return True
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return solveNQ()

# Run the solver
if __name__ == "__main__":
    solveNQ()
#"C:\Program Files\Python313\python.exe" H:\queen.py
#Enter the size of the board (N): 8

#Solution for N = 8
#1 0 0 0 0 0 0 0
#0 0 0 0 0 0 1 0
#0 0 0 0 1 0 0 0
#0 0 0 0 0 0 0 1
#0 1 0 0 0 0 0 0
#0 0 0 1 0 0 0 0
#0 0 0 0 0 1 0 0
#0 0 1 0 0 0 0 0

#Process finished with exit code 0