"""
Graph Practice: Directed Graph
==============================

Goal:
Practice directed graph representation and path search.


Undirected graph vs directed graph
----------------------------------

Undirected edge:

    A -- B

means:

    A can go to B
    B can go to A


Directed edge:

    A -> B

means:

    A can go to B
    but B cannot necessarily go back to A


Examples of directed graphs
---------------------------

- course prerequisites
- task dependencies
- web page links
- one-way roads


Tasks
-----

1. build_directed_graph(edges)

Build an adjacency list from directed edges.

Example:

    edges = [
        ("A", "B"),
        ("B", "C"),
        ("D", "A")
    ]

Should become:

    {
        "A": ["B"],
        "B": ["C"],
        "C": [],
        "D": ["A"]
    }

Important:

For directed graph, only add one direction:

    graph["A"].append("B")

Do not add:

    graph["B"].append("A")


2. has_directed_path(graph, start, target)

Return True if there is a path from start to target following edge direction.
Return False otherwise.

Example graph:

    D -> A -> B -> C

Then:

    has_directed_path(graph, "D", "C")
    # True

    has_directed_path(graph, "C", "D")
    # False


Expected output
---------------

{'A': ['B'], 'B': ['C'], 'C': [], 'D': ['A']}
True
False
"""


def build_directed_graph(edges):
    # TODO: Create empty graph dictionary.
    graph = {}
    # TODO: Loop through directed edges.
    for obj in edges:
        # TODO: Get node_a and node_b.
        node_a = obj[0]
        node_b = obj[1]
        # TODO: If node_a not in graph, create empty list.
        if node_a not in graph:
            graph[node_a] = []
        # TODO: If node_b not in graph, create empty list.
        if node_b not in graph:
            graph[node_b] = []
        # TODO: Add node_b to node_a's list only.
        graph[node_a].append(node_b)
    # TODO: Return graph.
    return graph


def has_directed_path(graph, start, target):
    # TODO: If start or target is not in graph, return False.
    if start not in graph or target not in graph:
        return False
    # TODO: Use DFS or BFS with visited set.
    visited = set()
    queue = [start]

    visited.add(start)

    while len(queue) > 0:
        node = queue.pop(0)
        
        if node == target:
            return True
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    # TODO: Follow only the directions stored in graph[node].
    return False


def main():
    edges = [
        ("A", "B"),
        ("B", "C"),
        ("D", "A")
    ]

    graph = build_directed_graph(edges)

    print(graph)
    print(has_directed_path(graph, "D", "C"))
    print(has_directed_path(graph, "C", "D"))


if __name__ == "__main__":
    main()
