"""
Heap / Priority Queue basic practice.

Goal:
1. Use heapq.heappush to add numbers into a min heap.
2. Use heap[0] to peek the current minimum.
3. Use heapq.heappop to pop all numbers in sorted order.

Run:
cd "/Users/eden1969/Documents/CS First years/10_heap_priority_queue"
python3 heap_basic.py
"""

import heapq


def build_min_heap(numbers):
    """
    Given a list of numbers, push each number into a heap.

    Return:
    - the heap list

    Hint:
    - start with heap = []
    - loop through numbers
    - use heapq.heappush(heap, num)
    """
    # TODO: write your code here
    heap = []
    for number in numbers:
        heapq.heappush(heap,number)
    return heap



def peek_min(heap):
    """
    Return the smallest value without removing it.

    Edge case:
    - if heap is empty, return None

    Hint:
    - in a min heap, heap[0] is the smallest value
    """
    # TODO: write your code here
    if not heap:
        return None
    return heap[0]


def pop_all_sorted(heap):
    """
    Pop every value from the heap and return them as a sorted list.

    Important:
    - heappop changes the heap
    - use while heap:
    """
    # TODO: write your code here
    result = []
    while heap: 
        smallest = heapq.heappop(heap)
        result.append(smallest)
    return result
        


def main():
    numbers = [5, 2, 8, 1, 9, 3]

    heap = build_min_heap(numbers)
    print("Original numbers:", numbers)
    print("Heap:", heap)
    print("Minimum:", peek_min(heap))
    print("Sorted by popping:", pop_all_sorted(heap))
    print("Heap after popping:", heap)

    print("\nExpected idea after you finish:")
    print("Minimum should be 1")
    print("Sorted by popping should be [1, 2, 3, 5, 8, 9]")


if __name__ == "__main__":
    main()
