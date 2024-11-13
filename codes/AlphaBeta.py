MAX, MIN = float('inf'), float('-inf')

def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    # Base case: when the depth is 3 (leaf nodes)
    if depth == 3:
        return values[nodeIndex]
    
    # Maximizing player (maximize the value)
    if maximizingPlayer:
        best = MIN
        for i in range(2):  # Check both child nodes
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            
            # Beta pruning: if beta is less than or equal to alpha, stop exploring
            if beta <= alpha:
                break
        return best
    else:
        # Minimizing player (minimize the value)
        best = MAX
        for i in range(2):  # Check both child nodes
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            
            # Beta pruning: if beta is less than or equal to alpha, stop exploring
            if beta <= alpha:
                break
        return best

if __name__ == "__main__":
    # Get the leaf node values from the user
    values_input = input("Enter the leaf node values separated by commas (e.g., 3, 5, 2, 9, 1, 4, 6, 7): ")
    values = list(map(int, values_input.split(',')))

    # Validate the input length (it should be 8 values for a tree of depth 3)
    expected_size = 2 ** 3  # 8 leaf nodes for depth 3
    if len(values) != expected_size:
        print(f"Error: You must enter exactly {expected_size} values.")
    else:
        # Call the minimax function starting from the root (index 0) and depth 0
        print("The optimal value is:", minimax(0, 0, True, values, MIN, MAX))

#output:
#Enter the leaf node values separated by commas (e.g., 3, 5, 2, 9, 1, 4, 6, 7): 5,4,3,2,1,0,-1,-2
#The optimal value is: 3
