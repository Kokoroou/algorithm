from typing import List, Union


def find_hamiltonian_path(graph: List[List[int]]) -> Union[List[int], None]:
    """
    Finds a Hamiltonian path in the given graph using a backtracking algorithm.

    Args:
        graph: The input graph represented as an adjacency matrix.

    Returns:
        The Hamiltonian path as a list of node indices. Returns None if no Hamiltonian path exists.
    """

    def is_valid(node: int, current_path: List[int]) -> bool:
        """
        Checks if the given node can be added to the current path.

        Args:
            node: The node to be added to the path.
            current_path: The current path.

        Returns:
            True if the node can be added to the path, False otherwise.
        """
        if node in current_path:
            return False
        if len(current_path) == 0 or graph[current_path[-1]][node] == 1:
            return True
        return False

    def find_path(current_path: List[int]) -> Union[List[int], None]:
        """
        Recursively finds a Hamiltonian path starting from the given path.

        Args:
            current_path: The current path.

        Returns:
            The Hamiltonian path as a list of node indices. Returns None if no Hamiltonian path exists.
        """
        # If the path includes every node in the graph, return it as a Hamiltonian path
        if len(current_path) == len(graph):
            return current_path

        # Otherwise, try to extend the path by adding a new node
        for node in range(len(graph)):
            if is_valid(node, current_path):
                new_path = current_path + [node]
                result_found = find_path(new_path)
                # If a Hamiltonian path is found, return it
                if result_found is not None:
                    return result_found

        # If no Hamiltonian path is found, return None
        return None

    # Start the search from each node in the graph
    for start_node in range(len(graph)):
        path = [start_node]
        result = find_path(path)
        # If a Hamiltonian path is found, return it
        if result is not None:
            return result

    # If no Hamiltonian path is found starting from any node, return None
    return None
