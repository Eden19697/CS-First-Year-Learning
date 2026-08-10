"""
Find the kth largest number with a min heap.

Core idea:
- Keep a min heap with at most k numbers.
- The heap stores the largest k candidates seen so far.
- After processing all numbers, heap[0] is the kth largest number.

Run:
cd "/Users/eden1969/Documents/CS First years/10_heap_priority_queue"
python3 kth_largest.py
"""

import heapq


def kth_largest(numbers, k):
    """
    Return the kth largest number.

    Example:
    numbers = [5, 1, 9, 3, 7, 2, 8]
    k = 3
    return 7

    Edge cases:
    - if k <= 0, return None
    - if k > len(numbers), return None

    Hint:
    - create heap = []
    - push each number into heap
    - if len(heap) > k, pop one value
    - at the end, heap has the largest k numbers
    - heap[0] is the kth largest number
    """
    # TODO: write your code here
    if k <= 0:
        return None
    if k > len(numbers):
        return None
    
    heap = []
    for number in numbers:
        heapq.heappush(heap,number)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


def main():
    numbers = [5, 1, 9, 3, 7, 2, 8]

    print("Numbers:", numbers)
    print("k = 1:", kth_largest(numbers, 1))
    print("k = 2:", kth_largest(numbers, 2))
    print("k = 3:", kth_largest(numbers, 3))
    print("k = 10:", kth_largest(numbers, 10))
    print("k = 0:", kth_largest(numbers, 0))

    print("\nExpected:")
    print("k = 1 -> 9")
    print("k = 2 -> 8")
    print("k = 3 -> 7")
    print("k = 10 -> None")
    print("k = 0 -> None")


if __name__ == "__main__":
    main()
