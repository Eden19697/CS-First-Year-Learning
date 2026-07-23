"""
Hash Table Practice: Contains Duplicate
=======================================

Goal:
Practice using a set for fast membership checking.


Task
----

Write this function:

    def contains_duplicate(numbers):
        ...


Return rules
------------

If the list contains any duplicate number:

    return True

If all numbers are unique:

    return False


Examples
--------

    contains_duplicate([1, 2, 3, 1])
    # True

    contains_duplicate([1, 2, 3, 4])
    # False


Hash table idea
---------------

Use a set:

    seen = set()

For each number:

    if number is already in seen:
        return True

    otherwise:
        add number to seen


Expected output
---------------

True
False
True
False
"""


def contains_duplicate(numbers):
    # TODO: Create a set to store seen numbers.
    seen = set()
    # TODO: Loop through numbers.
    for int in numbers:
        # TODO: If number is already in seen, return True.
        if int in seen:
            return True
        # TODO: Otherwise, add number to seen.
        else:
            seen.add(int)
    # TODO: If loop finishes, return False.
    return False


def main():
    print(contains_duplicate([1, 2, 3, 1]))
    print(contains_duplicate([1, 2, 3, 4]))
    print(contains_duplicate([7, 7]))
    print(contains_duplicate([]))


if __name__ == "__main__":
    main()
