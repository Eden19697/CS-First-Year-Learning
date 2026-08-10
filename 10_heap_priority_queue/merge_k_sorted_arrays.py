"""
Merge k sorted arrays with a min heap.

Core idea:
- Put the first value of each array into a min heap.
- Each heap item stores: (value, array_index, element_index)
- When you pop one value, push the next value from the same array.

Run:
cd "/Users/eden1969/Documents/CS First years/10_heap_priority_queue"
python3 merge_k_sorted_arrays.py
"""

import heapq


def merge_k_sorted_arrays(arrays):
    """
    Merge several sorted arrays into one sorted list.

    Example:
    arrays = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
    ]

    Return:
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    Edge cases:
    - if arrays is empty, return []
    - some inner arrays may be empty

    Hint:
    - create heap = []
    - push the first value of each non-empty array
    - use tuple: (value, array_index, element_index)
    - while heap:
        - pop the smallest value
        - append value to result
        - push the next value from the same array if it exists
    """
    # TODO: write your code here
    if not arrays:
        return []
    heap = []
    for index, array in enumerate(arrays):
        if array:
            value = array[0]
            heapq.heappush(heap,(value,index,0))
    result = []
    while len(heap) > 0:
        value, array_index, element_index = heapq.heappop(heap)
        result.append(value)

        next_index = element_index +1

        if next_index < len(arrays[array_index]):
            next_value = arrays[array_index][next_index]
            heapq.heappush(heap, (next_value,array_index,next_index))
    return result



def main():
    arrays = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
    ]

    arrays_with_empty = [
        [],
        [1, 3],
        [],
        [2, 4],
    ]

    print("Merged:", merge_k_sorted_arrays(arrays))
    print("Merged with empty arrays:", merge_k_sorted_arrays(arrays_with_empty))
    print("Merged empty input:", merge_k_sorted_arrays([]))

    print("\nExpected:")
    print("Merged: [1, 2, 3, 4, 5, 6, 7, 8, 9]")
    print("Merged with empty arrays: [1, 2, 3, 4]")
    print("Merged empty input: []")


if __name__ == "__main__":
    main()
