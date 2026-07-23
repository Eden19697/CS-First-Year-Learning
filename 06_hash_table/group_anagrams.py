"""
Hash Table Practice: Group Anagrams
===================================

Goal:
Practice using a dictionary to group related strings.


Task
----

Write this function:

    def group_anagrams(words):
        ...


Definition
----------

Anagrams are words that contain the same characters with the same frequencies,
but possibly in a different order.

Examples:

    "eat", "tea", "ate"

These are anagrams because they all contain:

    a, e, t


Return rules
------------

Return a list of groups.

Each group should contain words that are anagrams of each other.


Example
-------

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

Possible output:

    [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"]
    ]

The group order does not matter for this exercise.


Hash table idea
---------------

Use a dictionary:

    groups = {}

The key should identify the anagram pattern.

Simple key idea:

    sorted_word = "".join(sorted(word))

Examples:

    "eat" -> "aet"
    "tea" -> "aet"
    "ate" -> "aet"

So they go into the same group.


Pattern
-------

groups should look like:

    {
        "aet": ["eat", "tea", "ate"],
        "ant": ["tan", "nat"],
        "abt": ["bat"]
    }

At the end, return:

    list(groups.values())


Expected output
---------------

The exact group order may be different, but groups should be equivalent to:

[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
"""


def group_anagrams(words):
    # TODO: Create a dictionary for groups.
    groups = {}
    # TODO: Loop through each word.
    for word in words:
        # TODO: Create a key by sorting the letters in word.
        key = "".join(sorted(word))# # 把 list 里的字符重新拼成 string
        # TODO: If key is not in groups, create an empty list.
        if key not in groups:
            groups[key] = []
        # TODO: Append word to groups[key].
        groups[key].append(word)
    # TODO: Return list of all groups.
    return groups


def main():
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(group_anagrams(["abc", "bca", "cab", "dog"]))
    print(group_anagrams([]))


if __name__ == "__main__":
    main()
