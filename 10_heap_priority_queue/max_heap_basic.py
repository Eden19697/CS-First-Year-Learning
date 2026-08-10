"""
Simulate a max heap with heapq.

Python heapq is a min heap by default.
To get the largest number first, store negative numbers.

Example:
- push 5 as -5
- push 9 as -9
- heappop returns -9
- convert it back to 9

Run:
cd "/Users/eden1969/Documents/CS First years/10_heap_priority_queue"
python3 max_heap_basic.py
"""

import heapq


def build_max_heap(numbers):
    """
    Build a max heap by pushing negative numbers.

    Return:
    - the heap list containing negative values

    Hint:
    - create heap = []
    - for each number, push -number
    """
    # TODO: write your code here
    heap = []
    for number in numbers:
        heapq.heappush(heap,-number)
    return heap


def pop_max(heap):
    """
    Remove and return the largest number.

    Edge case:
    - if heap is empty, return None

    Hint:
    - heappop gives the smallest negative number
    - convert it back by using -
    """
    # TODO: write your code here
    if not heap:
        return None
    negative = heapq.heappop(heap)
    return -negative


def pop_all_descending(heap):
    """
    Pop all numbers from largest to smallest.

    Return:
    - a list sorted in descending order
    """
    # TODO: write your code here
    result = []
    while heap:
        largest = heapq.heappop(heap)
        result.append(-largest)
    return result


def main():
    numbers = [5, 1, 9, 3, 7, 2, 8]

    heap = build_max_heap(numbers)
    print("Numbers:", numbers)
    print("Max heap stored as negatives:", heap)
    print("Pop max:", pop_max(heap))
    print("Pop remaining descending:", pop_all_descending(heap))

    print("\nExpected:")
    print("Pop max: 9")
    print("Pop remaining descending: [8, 7, 5, 3, 2, 1]")


if __name__ == "__main__":
    main()
