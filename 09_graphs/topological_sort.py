"""
Graph Practice: Topological Sort
================================

Goal:
Practice topological sorting on a directed acyclic graph.


What is topological sort?
-------------------------

Topological sort is an ordering of nodes where every dependency comes before
the thing that depends on it.


Example: course prerequisites
-----------------------------

If:

    "Intro" -> "Data Structures"

means:

    You must take Intro before Data Structures.

Then "Intro" should appear before "Data Structures" in the result.


Important
---------

Topological sort only works cleanly on a DAG:

    Directed Acyclic Graph

That means:

    directed graph with no cycle


Example graph
-------------

graph = {
    "Intro": ["Data Structures", "Web"],
    "Data Structures": ["Algorithms"],
    "Web": ["Project"],
    "Algorithms": ["Project"],
    "Project": []
}

One valid topological order:

    ["Intro", "Data Structures", "Web", "Algorithms", "Project"]

Another valid order:

    ["Intro", "Web", "Data Structures", "Algorithms", "Project"]

Multiple correct answers are possible.


Kahn's algorithm idea
---------------------

1. Count indegree for each node.

indegree means:

    how many incoming edges a node has

Example:

    Intro -> Data Structures

Data Structures has indegree 1.


2. Start with all nodes whose indegree is 0.

These nodes have no prerequisites.


3. Repeatedly:

    pop a node from queue
    add it to result
    for each neighbor:
        reduce neighbor's indegree by 1
        if neighbor's indegree becomes 0:
            add it to queue


Expected output
---------------

One valid result:

['Intro', 'Data Structures', 'Web', 'Algorithms', 'Project']

Your result may be different but must respect dependencies.
"""


def topological_sort(graph):
    # TODO: Create indegree dictionary with every node starting at 0.
    indegree = {}

    for node in graph:
        indegree[node] = 0
    # TODO: Loop through graph and count incoming edges.
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1
    # TODO: Create queue with nodes whose indegree is 0.
    queue = []

    for node in indegree:
        if indegree[node] == 0:
            queue.append(node)
    # TODO: Create result list.
    result = []
    # TODO: While queue is not empty:
    while len(queue) > 0:
        # TODO: Pop first node.
        node = queue.pop(0)
        # TODO: Add node to result.
        result.append(node)
        # TODO: For each neighbor, reduce indegree.
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
        # TODO: If neighbor indegree becomes 0, append to queue.
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    # TODO: Return result.
    return result


def main():
    graph = {
        "Intro": ["Data Structures", "Web"],
        "Data Structures": ["Algorithms"],
        "Web": ["Project"],
        "Algorithms": ["Project"],
        "Project": []
    }

    print(topological_sort(graph))


if __name__ == "__main__":
    main()
