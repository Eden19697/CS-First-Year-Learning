"""
Heapify basic practice.

Core idea:
- heapq.heapify(numbers) changes an existing list into a min heap.
- After heapify, numbers[0] is the smallest value.
- heapify modifies the original list in place.

Run:
cd "/Users/eden1969/Documents/CS First years/10_heap_priority_queue"
python3 heapify_basic.py
"""

import heapq


def make_heap(numbers):
    """
    Convert a list into a min heap.

    Important:
    - heapq.heapify modifies the list in place
    - return the same list after heapify

    Hint:
    - use heapq.heapify(numbers)
    """
    # TODO: write your code here
    heapq.heapify(numbers)
    return numbers


def get_sorted_by_heapify(numbers):
    """
    Return all numbers in sorted order by using heapify + heappop.

    Important:
    - avoid changing the original input list
    - make a copy first

    Hint:
    - heap = numbers.copy()
    - heapify the copy
    - pop everything into result
    """
    # TODO: write your code here
    heap = numbers.copy()
    heapq.heapify(heap)
    result = []
    while len(heap) >0:
        num = heapq.heappop(heap)
        result.append(num)
    return result

def main():
    numbers = [5, 1, 9, 3, 7, 2, 8]

    heap = make_heap(numbers.copy())
    print("Heap:", heap)
    print("Minimum:", heap[0])
    print("Sorted:", get_sorted_by_heapify(numbers))
    print("Original numbers:", numbers)

    print("\nExpected:")
    print("Minimum: 1")
    print("Sorted: [1, 2, 3, 5, 7, 8, 9]")
    print("Original numbers should still be [5, 1, 9, 3, 7, 2, 8]")


if __name__ == "__main__":
    main()
