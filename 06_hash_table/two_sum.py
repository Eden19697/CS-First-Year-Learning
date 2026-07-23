"""
Hash Table Practice: Two Sum
============================

Goal:
Practice using a dictionary as a hash table for fast lookup.


Task
----

Write this function:

    def two_sum(numbers, target):
        ...


Given a list of integers and a target number, find two indexes such that:

    numbers[index1] + numbers[index2] == target


Return rules
------------

If a pair is found:

    return [index1, index2]

If no pair is found:

    return []


Important rule
--------------

You cannot use the same element twice.


Examples
--------

Example 1:

    numbers = [2, 7, 11, 15]
    target = 9

    2 + 7 = 9

    return [0, 1]


Example 2:

    numbers = [3, 2, 4]
    target = 6

    2 + 4 = 6

    return [1, 2]


Example 3:

    numbers = [3, 3]
    target = 6

    return [0, 1]


Hash table idea
---------------

Use a dictionary:

    seen = {}

The dictionary stores:

    number -> index

When you see a current number:

    needed = target - number

If needed is already in seen:

    you found the pair

Otherwise:

    store current number and index


Expected output
---------------

[0, 1]
[1, 2]
[0, 1]
[]
"""


def two_sum(numbers, target):
    # TODO: Create a dictionary to store seen numbers and their indexes.
    seen = {}
    # TODO: Loop through numbers with index.
    for index, value in enumerate(numbers):
        
        # TODO: Calculate needed number.
        needed = target - value
        # TODO: If needed number was seen before, return indexes.
        if needed in seen:
            return [seen[needed], index]
        # TODO: Store current number and index.
        seen[value] = index
    # TODO: If no pair found, return [].
    return []


def main():
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([3, 2, 4], 6))
    print(two_sum([3, 3], 6))
    print(two_sum([1, 2, 3], 10))


if __name__ == "__main__":
    main()
