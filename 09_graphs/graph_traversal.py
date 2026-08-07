"""
Graph Practice: DFS and BFS Traversal
=====================================

Goal:
Practice graph representation and traversal.


Tree vs Graph
-------------

A tree is a special kind of graph.

Tree:
- usually has a root
- has parent/child structure
- has no cycles

Graph:
- may not have a root
- nodes can connect in many ways
- can have cycles


Example graph
-------------

    Alice -- Bob
      |       |
    Charlie--David


Adjacency list representation
-----------------------------

graph = {
    "Alice": ["Bob", "Charlie"],
    "Bob": ["Alice", "David"],
    "Charlie": ["Alice", "David"],
    "David": ["Bob", "Charlie"]
}


Important idea: visited set
---------------------------

Graphs can have cycles.

Example:

    Alice -> Bob -> Alice -> Bob -> ...

So we need a visited set to avoid visiting the same node forever.


Tasks
-----

1. dfs(graph, start)

Depth-first search.

Go deep before coming back.

Use:
- visited set
- recursive helper or stack


2. bfs(graph, start)

Breadth-first search.

Visit level by level.

Use:
- visited set
- queue


3. has_path(graph, start, target)

Return True if there is a path from start to target.
Return False otherwise.

Example:

    has_path(graph, "Alice", "David")
    # True

because:

    Alice -> Bob -> David

    has_path(graph, "Alice", "Eve")
    # False


4. count_components(graph)

Count how many connected components are in the graph.

Example:

    graph = {
        "A": ["B"],
        "B": ["A"],
        "C": ["D"],
        "D": ["C"],
        "E": []
    }

There are 3 components:

    A-B
    C-D
    E


5. shortest_path(graph, start, target)

Return the shortest distance from start to target.

Use BFS because BFS visits nodes level by level.
The first time BFS reaches target, that distance is the shortest.

Example:

    shortest_path(graph, "Alice", "David")
    # 2

because:

    Alice -> Bob -> David

If no path exists, return -1.

Queue should store:

    (node, distance)

Example:

    queue = [("Alice", 0)]


6. build_graph(edges)

Build an adjacency list from an edge list.

Example:

    edges = [
        ("Alice", "Bob"),
        ("Alice", "Charlie"),
        ("Bob", "David"),
        ("Charlie", "David")
    ]

Should become:

    {
        "Alice": ["Bob", "Charlie"],
        "Bob": ["Alice", "David"],
        "Charlie": ["Alice", "David"],
        "David": ["Bob", "Charlie"]
    }

For an undirected graph, each edge should be added both ways:

    A -- B

means:

    graph["A"].append("B")
    graph["B"].append("A")


7. largest_component(graph)

Return the size of the largest connected component.

Example:

    graph = {
        "A": ["B"],
        "B": ["A"],
        "C": ["D", "E"],
        "D": ["C"],
        "E": ["C"],
        "F": []
    }

Components:

    A-B      size 2
    C-D-E    size 3
    F        size 1

Largest component size:

    3


Expected output
---------------

DFS order may vary depending on neighbor order, but should visit all nodes:

['Alice', 'Bob', 'David', 'Charlie']

BFS expected:

['Alice', 'Bob', 'Charlie', 'David']

True
False
3
2
-1
{'Alice': ['Bob', 'Charlie'], 'Bob': ['Alice', 'David'], 'Charlie': ['Alice', 'David'], 'David': ['Bob', 'Charlie']}
3
"""


def dfs(graph, start):
    # TODO: Create visited set.
    visited = set()
    # TODO: Create result list.
    result = []
    # TODO: Write recursive helper or use stack.
    def helper(node):
        visited.add(node)
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                helper(neighbor)
    # TODO: Return result.
    helper(start)
    return result


def bfs(graph, start):
    # TODO: Create visited set with start inside.
    visited = set()
    # TODO: Create queue with start inside.
    queue = [start]
    # TODO: Create result list.
    result = []
    visited.add(start)
    # TODO: While queue is not empty:
    while len(queue) > 0:
        # TODO: Pop first node.
        node = queue.pop(0)
        # TODO: Add node to result.
        result.append(node)
        # TODO: Loop through neighbors.
        for neighbor in graph[node]:
            # TODO: If neighbor not visited, mark visited and append to queue.
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    # TODO: Return result.
    return result


def has_path(graph, start, target):
    # TODO: Create visited set.
    visited = set()
    # TODO: Use DFS or BFS to search for target.
    def helper(node):
        if node == target:
            return True
        
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if helper(neighbor):
                    return True
        return False
    # TODO: Return True if target is found.
    if start not in graph:
        return False
    # TODO: Return False if search finishes and target was not found.
    return helper(start)


def count_components(graph):
    # TODO: Create visited set.
    visited = set()
    # TODO: Create count starting at 0.
    count = 0

    def visit(node):
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visit(neighbor)

    # TODO: Loop through every node in graph.
    for node in graph:
        # TODO: If node is not visited, this is a new component.
        if node not in visited:
        # TODO: Increase count.
                count += 1
        # TODO: Use DFS/BFS to mark all nodes in this component as visited.
                visit(node)
    # TODO: Return count.
    return count


def shortest_path(graph, start, target):
    # TODO: If start or target is not in graph, return -1.
    if start not in graph or target not in graph:  
        return -1
    # TODO: Create visited set with start inside.
    visited = set()
    visited.add(start)
    # TODO: Create queue with (start, 0).
    queue = [(start, 0)]

    # TODO: While queue is not empty:
    while len(queue) > 0:
        # TODO: Pop first item: node, distance.
        node, distance = queue.pop(0)
        # TODO: If node is target, return distance.
        if node == target:
            return distance
        # TODO: Loop through neighbors.
        for neighbors in graph[node]:
            # TODO: If neighbor not visited, mark visited and append (neighbor, distance + 1).
            if neighbors not in visited:
                visited.add(neighbors)
                queue.append((neighbors,distance+1))
        
    # TODO: If target was not found, return -1.
    return -1


def build_graph(edges):
    # TODO: Create empty graph dictionary.
    graph = {}
    # TODO: Loop through each edge.
    for connect in edges:
        # TODO: Get node_a and node_b from edge.
        node_a, node_b = connect
        # TODO: If node_a is not in graph, create empty list.
        if node_a not in graph:
            graph[node_a] = []
        # TODO: If node_b is not in graph, create empty list.
        if node_b not in graph:
            graph[node_b] = []
        # TODO: Add node_b to node_a's list.
        graph[node_a].append(node_b)
        # TODO: Add node_a to node_b's list.
        graph[node_b].append(node_a)
    # TODO: Return graph.
    return graph


def largest_component(graph):
    # TODO: Create visited set.
    visited = set()
    # TODO: Create largest starting at 0.
    largest = 0
    # TODO: Write helper that returns component size.
    def explore_size(node):
        visited.add(node)
        size = 1
    # TODO: Loop through every node.
        for neighbor in graph[node]:
        # TODO: If node is not visited, get component size.
            if neighbor not in visited:
        # TODO: Update largest if needed.
                size += explore_size(neighbor)
        return size
    
    for node in graph:
        if node not in visited:
            size = explore_size(node)
            if size > largest:
                largest = size
    # TODO: Return largest.
    return largest


def main():
    graph = {
        "Alice": ["Bob", "Charlie"],
        "Bob": ["Alice", "David"],
        "Charlie": ["Alice", "David"],
        "David": ["Bob", "Charlie"]
    }

    print(dfs(graph, "Alice"))
    print(bfs(graph, "Alice"))
    print(has_path(graph, "Alice", "David"))
    print(has_path(graph, "Alice", "Eve"))

    disconnected_graph = {
        "A": ["B"],
        "B": ["A"],
        "C": ["D"],
        "D": ["C"],
        "E": []
    }

    print(count_components(disconnected_graph))
    print(shortest_path(graph, "Alice", "David"))
    print(shortest_path(disconnected_graph, "A", "E"))

    edges = [
        ("Alice", "Bob"),
        ("Alice", "Charlie"),
        ("Bob", "David"),
        ("Charlie", "David")
    ]

    print(build_graph(edges))

    component_graph = {
        "A": ["B"],
        "B": ["A"],
        "C": ["D", "E"],
        "D": ["C"],
        "E": ["C"],
        "F": []
    }

    print(largest_component(component_graph))


if __name__ == "__main__":
    main()
