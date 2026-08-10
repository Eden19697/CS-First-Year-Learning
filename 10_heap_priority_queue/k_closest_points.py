"""
Find k closest points to the origin.

Core idea:
- Each point is (x, y).
- Distance to origin is sqrt(x*x + y*y).
- For comparison, we can use x*x + y*y without sqrt.
- Use a min heap storing: (distance, point)

Run:
cd "/Users/eden1969/Documents/CS First years/10_heap_priority_queue"
python3 k_closest_points.py
"""

import heapq


def distance_squared(point):
    """
    Return x*x + y*y.

    Example:
    point = (3, 4)
    return 25

    Hint:
    - unpack point into x and y
    """
    # TODO: write your code here
    return point[0]**2+point[1]**2


def k_closest_points(points, k):
    """
    Return the k closest points to the origin (0, 0).

    Example:
    points = [(1, 2), (3, 4), (0, 1)]
    k = 2
    return [(0, 1), (1, 2)] in any order

    Edge cases:
    - if k <= 0, return []
    - if points is empty, return []

    Hint:
    - create heap = []
    - for each point:
        - compute distance_squared(point)
        - push (distance, point) into heap
    - pop k points from heap
    - return only the points
    """
    # TODO: write your code here
    if k <= 0:
        return []
    if not points:
        return []
    heap = []
    result = []
    for point in points:
        distance = distance_squared(point)
        heapq.heappush(heap,(distance,point))
    while len(result) < k and heap:
        value = heapq.heappop(heap)
        result.append(value[1])
    return result


def main():
    points = [(1, 2), (3, 4), (0, 1), (2, 2)]

    print("Points:", points)
    print("k = 2:", k_closest_points(points, 2))
    print("k = 1:", k_closest_points(points, 1))
    print("k = 0:", k_closest_points(points, 0))
    print("empty:", k_closest_points([], 2))

    print("\nExpected:")
    print("k = 2 -> [(0, 1), (1, 2)] in any order")
    print("k = 1 -> [(0, 1)]")
    print("k = 0 -> []")
    print("empty -> []")


if __name__ == "__main__":
    main()
