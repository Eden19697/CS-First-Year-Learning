"""
Sorting Practice: Insertion Sort
================================

Goal:
Practice another basic sorting algorithm by hand.

Insertion sort idea:

    The left side is already sorted.
    Take one new value.
    Move it left until it is in the correct position.

This is similar to sorting playing cards in your hand.


Example
-------

numbers = [5, 3, 8, 1]

Start:

    [5, 3, 8, 1]

Round 1:

    Left side [5] is sorted.
    Take key = 3.
    3 should go before 5.

    [3, 5, 8, 1]

Round 2:

    Left side [3, 5] is sorted.
    Take key = 8.
    8 is already in the correct place.

    [3, 5, 8, 1]

Round 3:

    Left side [3, 5, 8] is sorted.
    Take key = 1.
    Move 8, 5, 3 to the right.
    Put 1 at the front.

    [1, 3, 5, 8]


Task
----

Write this function:

    def insertion_sort(numbers):
        ...


Return rules
------------

Return the sorted list.


Important variables
-------------------

i:
    The index of the new value we want to insert into the sorted left side.

key:
    The value we are trying to insert.

j:
    The index used to move left through the sorted part.


Core idea
---------

For each i starting from 1:

    key = numbers[i]
    j = i - 1

Then while j is valid and numbers[j] > key:

    move numbers[j] one step to the right
    j moves left

Finally:

    put key into the correct position


Expected output
---------------

[1, 3, 5, 8]
[7, 8, 9, 10]
[1, 2, 3]
[]
[4]
"""


def insertion_sort(numbers):
    # TODO: Start from index 1, because index 0 is already sorted by itself.
    for i in range(1, len(numbers)):
        # TODO: Store numbers[i] in key.
        key = numbers[i]
        # TODO: Set j to i - 1.
        j = i -1
        # TODO: While j is valid and numbers[j] is greater than key:
        while j >= 0 and numbers[j] > key:         
            numbers[j + 1] = numbers[j]
            j -= 1
            # TODO: Move numbers[j] one step to the right.

            # TODO: Move j one step to the left.

        # TODO: Put key in the correct position.
        numbers[j + 1] = key
    return numbers


def main():
    print(insertion_sort([5, 3, 8, 1]))
    print(insertion_sort([10, 9, 8, 7]))
    print(insertion_sort([1, 2, 3]))
    print(insertion_sort([]))
    print(insertion_sort([4]))


if __name__ == "__main__":
    main()
