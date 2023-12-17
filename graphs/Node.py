class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def build_graph(input_list):
    # Create a dictionary to store nodes by their values
    node_dict = {}

    # Create nodes without neighbors first
    for i in range(len(input_list)):
        node_val = i + 1
        node_dict[node_val] = Node(node_val)

    # Add neighbors to each node
    for i, neighbors_list in enumerate(input_list):
        current_node = node_dict[i + 1]
        current_node.neighbors = [node_dict[val] for val in neighbors_list]

    return node_dict[1] if node_dict else None


def print_graph(node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(
            f"Node {node.val} -> Neighbors: {[neighbor.val for neighbor in node.neighbors]}"
        )
        visited.add(node)

        for neighbor in node.neighbors:
            print_graph(neighbor, visited)
