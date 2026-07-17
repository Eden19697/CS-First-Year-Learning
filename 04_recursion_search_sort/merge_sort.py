"""
Sorting Practice: Merge Sort
============================

Goal:
Practice recursion and sorting together.

Merge sort idea:

    1. Split the list into two halves.
    2. Sort each half using recursion.
    3. Merge the two sorted halves.


Why merge sort matters
----------------------

Selection sort and insertion sort are usually:

    O(n^2)

Merge sort is:

    O(n log n)


Example
-------

numbers = [5, 3, 8, 1]

Split:

    [5, 3] and [8, 1]

Split again:

    [5] [3] [8] [1]

Merge:

    [3, 5] and [1, 8]

Merge again:

    [1, 3, 5, 8]


Task
----

Write two functions:

    def merge_sort(numbers):
        ...

    def merge(left, right):
        ...


merge_sort(numbers)
-------------------

Return a new sorted list.

Important parts:

1. Base case:

       if len(numbers) <= 1:
           return numbers

2. Split:

       mid = len(numbers) // 2
       left = numbers[:mid]
       right = numbers[mid:]

3. Recursively sort:

       sorted_left = merge_sort(left)
       sorted_right = merge_sort(right)

4. Merge:

       return merge(sorted_left, sorted_right)


merge(left, right)
------------------

Merge two already sorted lists into one sorted list.

Example:

    merge([3, 5], [1, 8])

Should return:

    [1, 3, 5, 8]


Important variables:

    i: index for left
    j: index for right
    result: merged list


Expected output
---------------

[1, 3, 5, 8]
[7, 8, 9, 10]
[1, 2, 3]
[]
[4]
[1, 1, 2, 3, 5]
"""


def merge(left, right):
    # TODO: Create result list.
    result = []
    # TODO: Create i and j pointers.
    i = 0
    j = 0
    # TODO: While both lists still have values:
    while (i < len(left)) and (j < len(right)):
        # TODO: Compare left[i] and right[j].
        if left[i] < right[j]:
        # TODO: Append the smaller value to result.
            result.append(left[i])
        # TODO: Move the pointer that was used.
            i += 1
        else:
            result.append(right[j])
            j += 1

    # TODO: Add remaining values from left.
    while i < len(left):
        result.append(left[i])
        i += 1
    # TODO: Add remaining values from right.
    while j < len(right):
        result.append(right[j])
        j += 1
    # TODO: Return result.
    return result


def merge_sort(numbers):
    # TODO: Base case. If list has 0 or 1 item, it is already sorted.
    if len(numbers) <= 1:
        return numbers
    # TODO: Find mid.
    mid = len(numbers)//2
    # TODO: Split into left and right.
    left = numbers[:mid]
    right = numbers[mid:]
    # TODO: Recursively sort left and right.
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    # TODO: Merge the sorted halves.
    return merge(sorted_left, sorted_right)


def main():
    print(merge_sort([5, 3, 8, 1]))
    print(merge_sort([10, 9, 8, 7]))
    print(merge_sort([1, 2, 3]))
    print(merge_sort([]))
    print(merge_sort([4]))
    print(merge_sort([3, 1, 2, 1, 5]))


if __name__ == "__main__":
    main()
