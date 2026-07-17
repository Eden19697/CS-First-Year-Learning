"""
Sorting Practice: Selection Sort
================================

Goal:
Practice writing a basic sorting algorithm by hand.

Selection sort idea:

    Each round, find the smallest value in the unsorted part.
    Then swap it into the current position.


Example
-------

numbers = [5, 3, 8, 1]

Round 1:

    Find the smallest value in [5, 3, 8, 1].
    Smallest is 1.
    Swap 1 with 5.

    [1, 3, 8, 5]

Round 2:

    Now the first value is sorted.
    Find the smallest value in [3, 8, 5].
    Smallest is 3.
    It is already in the right place.

    [1, 3, 8, 5]

Round 3:

    Find the smallest value in [8, 5].
    Smallest is 5.
    Swap 5 with 8.

    [1, 3, 5, 8]


Task
----

Write this function:

    def selection_sort(numbers):
        ...


Return rules
------------

Return the sorted list.


Important variables
-------------------

i:
    The current position where the next smallest value should go.

min_index:
    The index of the smallest value found so far.

j:
    The index used to scan the rest of the list.


Useful swap syntax
------------------

    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]


Expected output
---------------

[1, 3, 5, 8]
[7, 8, 9, 10]
[1, 2, 3]
[]
[4]
"""


def selection_sort(numbers):
    # TODO: Loop through each position i.
    
    for i in range(len(numbers)):   
        min_index = i
        
        for j in range(i+1, len(numbers)):
            # TODO: Assume i is the index of the smallest value.
            if numbers[j] < numbers[min_index]:
                min_index = j

        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]#必须要用 numbers[]这种格式才是交换

        # TODO: Search the rest of the list for a smaller value.

        # TODO: If you find a smaller value, update min_index.

        # TODO: Swap numbers[i] with numbers[min_index].

    return numbers


def main():
    print(selection_sort([5, 3, 8, 1]))
    print(selection_sort([10, 9, 8, 7]))
    print(selection_sort([1, 2, 3]))
    print(selection_sort([]))
    print(selection_sort([4]))


if __name__ == "__main__":
    main()
