"""
Hash Table Practice: First Unique Character
===========================================

Goal:
Practice dictionary counting and preserving original order.


Task
----

Write this function:

    def first_unique_char(text):
        ...


Return rules
------------

Return the first character that appears exactly once.

If there is no unique character:

    return None


Examples
--------

    first_unique_char("leetcode")
    # "l"

    first_unique_char("loveleetcode")
    # "v"

    first_unique_char("aabb")
    # None


Hash table idea
---------------

Use a dictionary to count characters.

Step 1:
    Count every character.

Step 2:
    Loop through the original text again.
    Return the first character whose count is 1.


Expected output
---------------

l
v
None
a
"""


def first_unique_char(text):
    # TODO: Create a dictionary for character counts.
    dict = {}
    # TODO: First pass: count each character.
    for index, value in enumerate(text):
        if value not in dict:
            dict[value] = 1
        else:
            dict[value] += 1
    # TODO: Second pass: find the first character whose count is 1.
    for index, value in enumerate(text):
        if dict[value] == 1:
            return value
    # TODO: If no unique character exists, return None.
    return None


def main():
    print(first_unique_char("leetcode"))
    print(first_unique_char("loveleetcode"))
    print(first_unique_char("aabb"))
    print(first_unique_char("abcabcade"))


if __name__ == "__main__":
    main()
