def get_user_input():

    start_node = input("Enter the start node: ")
    stop_node = input("Enter the stop node: ")

    # Get the graph nodes and their neighbors from the user
    graph_nodes = {}
    while True:
        node = input("Enter a node (or 'done' to finish): ")
        if node.lower() == 'done':
            break
        neighbors = input(f"Enter the neighbors of {node} in the format 'neighbor1,weight1;neighbor2,weight2' (or 'none' if no neighbors): ")
        if neighbors.lower() == 'none':
            graph_nodes[node] = None
        else:
            neighbors_list = []
            for neighbor in neighbors.split(';'):
                n, weight = neighbor.split(',')
                neighbors_list.append((n, int(weight)))
            graph_nodes[node] = neighbors_list

    # Get the heuristic values from the user
    heuristic_values = {}
    for node in graph_nodes:
        heuristic_value = int(input(f"Enter the heuristic value for {node}: "))
        heuristic_values[node] = heuristic_value

    return start_node, stop_node, graph_nodes, heuristic_values

def aStarAlgo(start_node, stop_node, graph_nodes, heuristic_values):
    open_set = set([start_node])
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}

    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n == None or g[v] + heuristic_values[v] < g.get(n, float('inf')) + heuristic_values.get(n, float('inf')):
                n = v
        if n == stop_node or graph_nodes.get(n) == None:
            pass
        else:
            for m, weight in graph_nodes.get(n, []):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g.get(m, float('inf')) > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n == None:
            print('Path does not exist!')
            return None
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path
        open_set.remove(n)
        closed_set.add(n)
    print('Path does not exist!')
    return None

def main():
    start_node, stop_node, graph_nodes, heuristic_values = get_user_input()
    print("\nGraph Nodes:")
    for node, neighbors in graph_nodes.items():
        print(f"{node}: {neighbors}")
    print("\nHeuristic Values:")
    for node, heuristic in heuristic_values.items():
        print(f"{node}: {heuristic}")
    aStarAlgo(start_node, stop_node, graph_nodes, heuristic_values)

if __name__ == "__main__":
    main()


#OUTPUT
#Enter the start node: A
#Enter the stop node: G
#Enter a node (or 'done' to finish): A
#Enter the neighbors of A in the format 'neighbor1,weight1;neighbor2,weight2' (or 'none' if no neighbors): B,2;E,3
#Enter a node (or 'done' to finish): B
#Enter the neighbors of B in the format 'neighbor1,weight1;neighbor2,weight2' (or 'none' if no neighbors): C,1;G,9
#Enter a node (or 'done' to finish): C
#Enter the neighbors of C in the format 'neighbor1,weight1;neighbor2,weight2' (or 'none' if no neighbors): none
#Enter a node (or 'done' to finish): E
#Enter the neighbors of E in the format 'neighbor1,weight1;neighbor2,weight2' (or 'none' if no neighbors): D,6
#Enter a node (or 'done' to finish): D
#Enter the neighbors of D in the format 'neighbor1,weight1;neighbor2,weight2' (or 'none' if no neighbors): G,1
#Enter a node (or 'done' to finish): G
#Enter the neighbors of G in the format 'neighbor1,weight1;neighbor2,weight2' (or 'none' if no neighbors): none
#Enter a node (or 'done' to finish): done
#Enter the heuristic value for A: 11
#Enter the heuristic value for B: 6
#Enter the heuristic value for C: 99
#Enter the heuristic value for E: 7
#Enter the heuristic value for D: 1
#Enter the heuristic value for G: 0

#Graph Nodes:
#A: [('B', 2), ('E', 3)]
#B: [('C', 1), ('G', 9)]
#C: None
#E: [('D', 6)]
#D: [('G', 1)]
#G: None

#Heuristic Values:
#A: 11
#B: 6
#C: 99
#E: 7
#D: 1
#G: 0

#Path found: ['A', 'E', 'D', 'G']