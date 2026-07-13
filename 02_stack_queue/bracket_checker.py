"""
Stack Practice: Bracket Checker
===============================

Goal:
Practice using a stack to solve a real checking problem.

A stack follows this rule:

    Last In, First Out

In this exercise, you will check whether brackets in a string are balanced.

The brackets are:

    ()
    []
    {}


Examples
--------

Balanced examples:

    "()"
    "([])"
    "{[()]}"
    "a + (b * [c + d])"

These should return:

    True


Unbalanced examples:

    "("
    ")"
    "([)]"
    "{[(])}"

These should return:

    False


Task
----

Write this function:

    def is_balanced(text):
        ...


Rules
-----

1. If you see an opening bracket:

       (
       [
       {

   push it into the stack.


2. If you see a closing bracket:

       )
       ]
       }

   check whether it matches the latest opening bracket.

   Example:

       ")" must match "("
       "]" must match "["
       "}" must match "{"


3. If a closing bracket appears but the stack is empty:

       return False


4. If a closing bracket does not match the top of the stack:

       return False


5. At the end:

   if the stack is empty:
       return True
   else:
       return False


Hints
-----

You may want to use:

    stack = []

    stack.append(char)
    stack.pop()
    stack[-1]


You may also want a dictionary like this:

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }


Suggested structure
-------------------

def is_balanced(text):
    # TODO: Use stack to check brackets
    pass


def main():
    examples = [
        "()",
        "([])",
        "{[()]}",
        "a + (b * [c + d])",
        "(",
        ")",
        "([)]",
        "{[(])}",
    ]

    for text in examples:
        print(text, is_balanced(text))


if __name__ == "__main__":
    main()


Expected output
---------------

() True
([]) True
{[()]} True
a + (b * [c + d]) True
( False
) False
([)] False
{[(])} False
"""


def is_balanced(text):
    # TODO: Use stack to check brackets.
    Balance = True
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    stack = []

    for char in text:
        if char in "([{":
            stack.append(char)

        elif char in ")]}":
            if not stack:
                return False
            if stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0#防止“（（”这种情况




def main():
    examples = [
        "()",
        "([])",
        "{[()]}",
        "a + (b * [c + d])",
        "(",
        ")",
        "([)]",
        "{[(])}",
    ]

    for text in examples:
        print(text, is_balanced(text))


if __name__ == "__main__":
    main()
