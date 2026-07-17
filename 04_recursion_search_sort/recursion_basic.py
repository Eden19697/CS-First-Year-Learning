"""
Recursion Practice: Basic Recursive Functions
=============================================

Goal:
Practice the basic idea of recursion.

Recursion means:

    A function calls itself.

Every recursive function needs two parts:

1. Base case
   - When should the recursion stop?

2. Recursive case
   - How do we make the problem smaller?


Task 1: factorial(n)
--------------------

Factorial means:

    5! = 5 * 4 * 3 * 2 * 1

Examples:

    factorial(0) -> 1
    factorial(1) -> 1
    factorial(5) -> 120

Rules:

    factorial(0) == 1
    factorial(1) == 1

Recursive relationship:

    factorial(n) = n * factorial(n - 1)


Task 2: sum_to_n(n)
-------------------

sum_to_n means:

    sum_to_n(5) = 1 + 2 + 3 + 4 + 5

Examples:

    sum_to_n(0) -> 0
    sum_to_n(1) -> 1
    sum_to_n(5) -> 15

Rule:

    sum_to_n(0) == 0

Recursive relationship:

    sum_to_n(n) = n + sum_to_n(n - 1)


Expected output
---------------

1
1
120
0
1
15
"""


def factorial(n):
    # TODO: Base case.
    if n == 0:
        return 1
    # TODO: Recursive case.
    return  n * factorial(n - 1)


def sum_to_n(n):
    # TODO: Base case.
    if n == 0:
        return 0
    # TODO: Recursive case.
    return n + sum_to_n(n-1)


def main():
    print(factorial(0))
    print(factorial(1))
    print(factorial(5))

    print(sum_to_n(0))
    print(sum_to_n(1))
    print(sum_to_n(5))


if __name__ == "__main__":
    main()
