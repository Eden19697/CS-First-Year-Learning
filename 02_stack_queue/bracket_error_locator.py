"""
Stack Practice: Bracket Error Locator
=====================================

Goal:
Practice stack again, but this time report where the bracket error happens.

This exercise is similar to bracket_checker.py, but it returns an error message
instead of only True or False.


Task
----

Write this function:

    def check_brackets(text):
        ...


Return rules
------------

If all brackets are balanced, return:

    "OK"


If there is an extra closing bracket, return:

    "Extra closing bracket at index X"

Example:

    check_brackets(")")
    # "Extra closing bracket at index 0"


If there is an opening bracket that was never closed, return:

    "Unclosed opening bracket at index X"

Example:

    check_brackets("(")
    # "Unclosed opening bracket at index 0"


If a closing bracket does not match the latest opening bracket, return:

    "Mismatched bracket at index X"

Example:

    check_brackets("(]")
    # "Mismatched bracket at index 1"


Examples
--------

    check_brackets("()")
    # "OK"

    check_brackets("([{}])")
    # "OK"

    check_brackets(")")
    # "Extra closing bracket at index 0"

    check_brackets("(")
    # "Unclosed opening bracket at index 0"

    check_brackets("(]")
    # "Mismatched bracket at index 1"

    check_brackets("a + (b * [c + d])")
    # "OK"

    check_brackets("a + (b * [c + d)")
    # "Mismatched bracket at index 16"


Important hint
--------------

In the previous exercise, the stack could store only bracket characters:

    stack.append(char)

In this exercise, store both the bracket and its index:

    stack.append((char, index))

Example:

    ("(", 4)

This helps you report where an unclosed opening bracket happened.


Useful tools
------------

enumerate(text):

    for index, char in enumerate(text):
        ...


stack operations:

    stack.append((char, index))
    top_char, top_index = stack.pop()


dictionary for matching:

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }


Expected output
---------------

() => OK
([{}]) => OK
) => Extra closing bracket at index 0
( => Unclosed opening bracket at index 0
(] => Mismatched bracket at index 1
a + (b * [c + d]) => OK
a + (b * [c + d) => Mismatched bracket at index 16
{[(])} => Mismatched bracket at index 3
"""


def check_brackets(text):
    stack = []

    opening = "([{"

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for index, char in enumerate(text):
        # TODO: If char is an opening bracket, push (char, index).
        if char in opening:
            stack.append((char, index))



        # TODO: If char is a closing bracket:
        # 1. If stack is empty, return extra closing bracket message.
        # 2. Otherwise pop the latest opening bracket.
        # 3. If it does not match, return mismatched bracket message.
        elif char in pairs:
            if stack == []:
                return f"Extra closing bracket at index {index}"
            
            top_char, top_index = stack.pop()
            if top_char != pairs[char]:
                return f"Mismatched bracket at index {index}"
            

    
    if len(stack) != 0:
        top_char, top_index = stack[-1]
        return f"Unclosed opening bracket at index {top_index}"
    # TODO: If stack is not empty, return unclosed opening bracket message.
        
    return "OK"


def main():
    examples = [
        "()",
        "([{}])",
        ")",
        "(",
        "(]",
        "a + (b * [c + d])",
        "a + (b * [c + d)",
        "{[(])}",
    ]

    for text in examples:
        print(text, "=>", check_brackets(text))


if __name__ == "__main__":
    main()
