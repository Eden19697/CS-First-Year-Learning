"""
Hash Table Practice: Intersection of Two Lists
==============================================

Goal:
Practice using sets to find common values.


Task
----

Write this function:

    def intersection(nums1, nums2):
        ...


Return rules
------------

Return the numbers that appear in both lists.

Each number should appear only once in the result.

The order does not matter for this exercise.


Examples
--------

    intersection([1, 2, 2, 3], [2, 2, 4])
    # [2]

    intersection([4, 9, 5], [9, 4, 9, 8, 4])
    # [9, 4]


Hash table idea
---------------

Use a set for fast lookup and deduplication.

Idea:

    set1 = set(nums1)
    result = set()

For every number in nums2:

    if number is in set1:
        add it to result

At the end:

    return list(result)


Expected output
---------------

[2]
[9, 4] or [4, 9]
[]
"""


def intersection(nums1, nums2):
    # TODO: Convert nums1 to a set.
    a = set()
    for int in nums1:
        a.add(int)
    # TODO: Create result set.
    result = set()
    # TODO: Loop through nums2.
    for int in nums2:
        # TODO: If number is in set1, add it to result.
        if int in a:
            result.add(int)
    # TODO: Return result as a list.
    return list(result)


def main():
    print(intersection([1, 2, 2, 3], [2, 2, 4]))
    print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
    print(intersection([1, 2, 3], [4, 5, 6]))


if __name__ == "__main__":
    main()
