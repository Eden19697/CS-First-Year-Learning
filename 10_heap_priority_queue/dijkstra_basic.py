"""
Dijkstra shortest path basic practice.

Core idea:
- Use a min heap to always process the node with the smallest known distance.
- Heap item: (distance, node)
- Works for graphs with non-negative edge weights.

Run:
cd "/Users/eden1969/Documents/CS First years/10_heap_priority_queue"
python3 dijkstra_basic.py
"""

import heapq


def dijkstra(graph, start):
    """
    Return the shortest distance from start to every reachable node.

    Graph format:
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("D", 5)],
        "C": [("B", 1), ("D", 8)],
        "D": [],
    }

    Return example from start "A":
    {
        "A": 0,
        "C": 2,
        "B": 3,
        "D": 8
    }

    Hint:
    - distances = {start: 0}
    - heap = [(0, start)]
    - while heap:
        - pop current_distance, current_node
        - if current_distance is larger than distances[current_node], skip it
        - loop through neighbors
        - new_distance = current_distance + weight
        - if neighbor not in distances or new_distance is smaller:
            - update distances[neighbor]
            - push (new_distance, neighbor)
    """
    # TODO: write your code here
    distances = {start:0}
    heap = [(0,start)]
    
    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.get(current_node,[]):
            #从 graph 字典里拿 current_node 对应的邻居列表；
            #如果 current_node 不在 graph 里，就返回空 list []。
            new_distance = current_distance + weight
            
            if neighbor not in distances or new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))

    return distances


def shortest_distance(graph, start, target):
    """
    Return the shortest distance from start to target.

    Edge case:
    - if target is unreachable, return None

    Hint:
    - call dijkstra(graph, start)
    - return distances.get(target)
    """
    # TODO: write your code here
    if target not in graph:
        return None
    distances = dijkstra(graph,start)
    return distances.get(target)


def main():
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("D", 5)],
        "C": [("B", 1), ("D", 8)],
        "D": [],
        "E": [("A", 1)],
    }

    print("Distances from A:", dijkstra(graph, "A"))
    print("A to D:", shortest_distance(graph, "A", "D"))
    print("A to E:", shortest_distance(graph, "A", "E"))

    print("\nExpected:")
    print("Distances from A -> {'A': 0, 'C': 2, 'B': 3, 'D': 8}")
    print("A to D -> 8")
    print("A to E -> None")


if __name__ == "__main__":
    main()
