"""
Search Practice: Binary Search
==============================

Goal:
Practice binary search on a sorted list.

Binary search only works when the list is already sorted.

It repeatedly checks the middle value and removes half of the search space.


Task
----

Write this function:

    def binary_search(numbers, target):
        ...


Return rules
------------

If target is found:

    return its index

If target is not found:

    return -1


Example
-------

numbers = [1, 3, 5, 7, 9, 11, 13]

binary_search(numbers, 7)
# 3

Because:

numbers[3] == 7


binary_search(numbers, 2)
# -1

Because 2 is not in the list.


Core idea
---------

Use three positions:

    left
    right
    mid


Start:

    left = 0
    right = len(numbers) - 1


Middle:

    mid = (left + right) // 2


If:

    numbers[mid] == target

then you found the target.


If:

    numbers[mid] < target

then target must be on the right side:

    left = mid + 1


If:

    numbers[mid] > target

then target must be on the left side:

    right = mid - 1


Expected output
---------------

3
0
6
-1
-1
"""


def binary_search(numbers, target):
    # TODO: Create left and right pointers.
    left = 0
    right = len(numbers)-1
    # TODO: While left <= right.
    while left <= right:
        # TODO: Calculate mid.
        mid = int((left+right)/2)
        # TODO: If numbers[mid] == target, return mid.
        if numbers[mid] == target:
            return mid
        # TODO: If numbers[mid] < target, search right half.
        elif numbers[mid] < target:
            left = mid + 1
        # TODO: Otherwise, search left half.
        else:
            right = mid - 1

    # TODO: Return -1 if not found.
    return -1


def main():
    numbers = [1, 3, 5, 7, 9, 11, 13]

    print(binary_search(numbers, 7))
    print(binary_search(numbers, 1))
    print(binary_search(numbers, 13))
    print(binary_search(numbers, 2))
    print(binary_search(numbers, 20))


if __name__ == "__main__":
    main()
