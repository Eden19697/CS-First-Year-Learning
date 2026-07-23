"""
Hash Table Practice: Valid Anagram
==================================

Goal:
Practice using dictionaries to compare character frequencies.


Task
----

Write this function:

    def is_anagram(s, t):
        ...


Definition
----------

Two strings are anagrams if they contain the same characters with the same
frequencies, but possibly in a different order.


Examples
--------

    is_anagram("listen", "silent")
    # True

    is_anagram("rat", "car")
    # False

    is_anagram("aabb", "baba")
    # True


Hash table idea
---------------

Use dictionaries to count characters.

Method 1:

    count_s = {}
    count_t = {}

Count characters in s.
Count characters in t.

Then compare:

    count_s == count_t


Expected output
---------------

True
False
True
False
"""


def is_anagram(s, t):
    # TODO: Create two dictionaries.
    book1 = {}
    book2 = {}
    # TODO: Count characters in s.
    for i in s:
        if i not in book1:
            book1[i] = 1
        else:
            book1[i] += 1
    # TODO: Count characters in t.
    for j in t:
        if j not in book2:
            book2[j] = 1
        else:
            book2[j] += 1
    # TODO: Return whether the two dictionaries are equal.
    return book1 == book2

def main():
    print(is_anagram("listen", "silent"))
    print(is_anagram("rat", "car"))
    print(is_anagram("aabb", "baba"))
    print(is_anagram("hello", "helo"))


if __name__ == "__main__":
    main()
