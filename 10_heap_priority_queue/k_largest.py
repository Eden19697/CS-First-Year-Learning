"""
Find the k largest numbers with a min heap.

Core idea:
- Keep a min heap with at most k numbers.
- The heap stores the best k candidates seen so far.
- If the heap size is bigger than k, pop the smallest one.

Run:
cd "/Users/eden1969/Documents/CS First years/10_heap_priority_queue"
python3 k_largest.py
"""

import heapq


def find_k_largest(numbers, k):
    """
    Return the k largest numbers.

    Example:
    numbers = [5, 1, 9, 3, 7, 2, 8]
    k = 3
    return [7, 8, 9]

    Edge cases:
    - if k <= 0, return []
    - if k >= len(numbers), return all numbers in sorted order

    Hint:
    - create heap = []
    - push each number into heap
    - if len(heap) > k, pop one value
    - at the end, the heap contains the k largest numbers
    - return sorted(heap)
    """
    # TODO: write your code here
    if k <= 0:
        return []
    if k >= len(numbers):
        return sorted(numbers)
    
    heap = []
    for number in numbers:
        heapq.heappush(heap,number)
        if len(heap) > k:
            heapq.heappop(heap)
    return sorted(heap)


def main():
    numbers = [5, 1, 9, 3, 7, 2, 8]

    print("Numbers:", numbers)
    print("k = 3:", find_k_largest(numbers, 3))
    print("k = 1:", find_k_largest(numbers, 1))
    print("k = 0:", find_k_largest(numbers, 0))
    print("k = 10:", find_k_largest(numbers, 10))

    print("\nExpected:")
    print("k = 3 -> [7, 8, 9]")
    print("k = 1 -> [9]")
    print("k = 0 -> []")
    print("k = 10 -> [1, 2, 3, 5, 7, 8, 9]")


if __name__ == "__main__":
    main()
