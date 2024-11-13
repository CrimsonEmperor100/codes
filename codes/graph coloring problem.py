# Function to check if it is safe to color vertex 'v' with color 'c'
def is_safe(graph, colors, v, c):
    for neighbor in graph[v]:
        if colors[neighbor] == c:  # Check if any adjacent vertex has the same color
            return False
    return True


def graph_coloring_util(graph, colors, v, color_list):

    if v == len(graph):
        return True

    # Try all colors for vertex 'v'
    for c in color_list:
        if is_safe(graph, colors, v, c):
            colors[v] = c  # Assign color 'c' to vertex 'v'


            if graph_coloring_util(graph, colors, v + 1, color_list):
                return True


            colors[v] = None

    return False


def main():
    # Input the number of vertices
    num_vertices = int(input("Enter the number of vertices: "))

    # Input the adjacency list
    print("Enter the adjacency list:")
    graph = []
    for i in range(num_vertices):
        neighbors = list(map(int, input(f"Neighbors of vertex {i}: ").split()))
        graph.append(neighbors)


    color_list = input("Enter the list of colors separated by space: ").split()


    colors = [None] * len(graph)

    # Solve the graph coloring problem starting from vertex 0
    if not graph_coloring_util(graph, colors, 0, color_list):
        print("Solution does not exist")
    else:
        for i in range(len(graph)):
            print(f"Vertex {i}: {colors[i]}")


if __name__ == "__main__":
    main()
# Output process based on the input:
# Enter the number of vertices: 4
# Enter the adjacency list:
# Neighbors of vertex 0: 1 2
# Neighbors of vertex 1: 0 2 3
# Neighbors of vertex 2: 0 1
# Neighbors of vertex 3: 1
# Enter the list of colors separated by space: Red Green Blue

# The adjacency list represents the graph:
# Vertex 0 is connected to vertices 1 and 2
# Vertex 1 is connected to vertices 0, 2, and 3
# Vertex 2 is connected to vertices 0 and 1
# Vertex 3 is connected to vertex 1

# The program will now attempt to assign colors from the list ["Red", "Green", "Blue"]

# Final color assignment:
# Vertex 0: Red
# Vertex 1: Green
# Vertex 2: Blue
# Vertex 3: Red
