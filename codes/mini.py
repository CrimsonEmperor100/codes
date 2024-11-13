from jinja2.nodes import Output

player, opponent = 'x', 'o'

# Check if there are moves left on the board
def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True
    return False

# Evaluate the board for a win/loss/draw
def evaluate(b):
    for row in range(3):
        if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
            if b[row][0] == player:
                return 10
            elif b[row][0] == opponent:
                return -10

    for col in range(3):
        if b[0][col] == b[1][col] and b[1][col] == b[2][col]:
            if b[0][col] == player:
                return 10
            elif b[0][col] == opponent:
                return -10

    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:
        if b[0][0] == player:
            return 10
        elif b[0][0] == opponent:
            return -10

    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:
        if b[0][2] == player:
            return 10
        elif b[0][2] == opponent:
            return -10

    return 0

# Minimax algorithm
def minimax(board, depth, isMax):
    score = evaluate(board)

    if score == 10:
        return score
    if score == -10:
        return score
    if not isMovesLeft(board):
        return 0

    if isMax:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = player
                    best = max(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = '_'
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = opponent
                    best = min(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = '_'
        return best

# Find the best move for the player
def findBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = player
                moveVal = minimax(board, 0, False)
                board[i][j] = '_'
                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal
    print("The value of the best Move is:", bestVal)
    return bestMove

# Accept user input for the board configuration
def getUserInput():
    print("Enter the Tic-Tac-Toe board configuration (use 'x', 'o', '_'):")
    board = []
    for i in range(3):
        row = input(f"Enter row {i + 1} (e.g., x o _): ").split()
        if len(row) != 3 or any(cell not in ['x', 'o', '_'] for cell in row):
            print("Invalid input! Please enter 3 characters ('x', 'o', '_') separated by spaces.")
            return getUserInput()
        board.append(row)
    return board

# Main function
def main():
    board = getUserInput()
    print("\nThe current board is:")
    for row in board:
        print(" ".join(row))
    bestMove = findBestMove(board)
    print("\nThe Optimal Move is:")
    print("ROW:", bestMove[0], "COL:", bestMove[1])

if __name__ == "__main__":
    main()

#Output
#Enter the Tic-Tac-Toe board configuration (use 'x', 'o', '_'):
#Enter row 1 (e.g., x o _): x o x
#Enter row 2 (e.g., x o _): o x o
#Enter row 3 (e.g., x o _): x x x

#The current board is:
#x o x
#o x o
#x x x
#The value of the best Move is: -1000

#The Optimal Move is:
#ROW: -1 COL: -1
