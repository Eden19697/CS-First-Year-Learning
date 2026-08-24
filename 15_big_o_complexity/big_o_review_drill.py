"""Big-O review drill.

Goal:
- Distinguish sequential code from nested code.
- Recognize O(log n) when a range is repeatedly halved.
- Recognize when a list, dict, or set costs O(n) extra space.

How to use:
1. For each function, write its time and extra-space complexity in the docstring.
2. Complete the TODO sections without reopening big_o_examples.py.
3. Run this file and compare the output with the expected results.
4. Send your completed file for a code review.
"""


def maximum_number(numbers):
    """Return the largest number.

    Time: O(n)
    Extra space: O(1)
    Reason: We scan the list once and keep only the current largest value.
    """
    # TODO: return None for an empty list.
    # TODO: scan once while tracking the largest value seen so far.
    if not numbers:
        return None
    largest = -float("inf")
    for i in numbers:
        if i > largest:
            largest = i
    return largest


def contains_duplicate_bruteforce(numbers):
    """Return whether a list contains a duplicate.

    Time: O(n^2)
    Extra space: O(1)
    Reason: We compare every pair of elements without using extra data structures.
    """
    # TODO: compare each number with every later number.
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                return True

    return False


def contains_duplicate_with_set(numbers):
    """Return whether a list contains a duplicate.

    Time: O(n)
    Extra space: O(n)
    Reason: We scan the list once and store each number in a set. 
    Set lookup is O(1) on average, and the set may contain up to n elements.
    """
    # TODO: use a set named seen.
    seen = set()

    for i in numbers:
        if i in seen:
            return True

        seen.add(i)

    return False

def binary_search(numbers, target):
    """Return target's index in sorted numbers, or -1.

    Time: O(log n)
    Extra space: O(1)
    Reason: Each step removes half of the remaining search space.
    """
    # TODO: use left, right, and middle.
    # TODO: after checking middle, discard the half that cannot contain target.
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = left + (right - left)//2

        if numbers[mid] == target:
            return mid

        elif numbers[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


def sort_then_find(numbers, target):
    """Return whether target is present after sorting numbers.

    Time: O(n log n)
    Extra space: O(n)
    Reason: Sorting takes O(n log n), then we scan the sorted list once in O(n). 
    The sorted copy uses O(n) extra space.
    """
    # TODO: create sorted_numbers with sorted(numbers).
    # TODO: scan sorted_numbers once for target.
    sorted_numbers = sorted(numbers)

    for number in sorted_numbers:
        if number == target:
            return True

    return False


def main():
    print("1. maximum number:", maximum_number([4, 9, 2, 7]))
    print("   Expected: 9")

    print("2. brute-force duplicate:", contains_duplicate_bruteforce([1, 2, 3, 2]))
    print("   Expected: True")

    print("3. set duplicate:", contains_duplicate_with_set([1, 2, 3, 4]))
    print("   Expected: False")

    print("4. binary search:", binary_search([1, 3, 5, 7, 9], 7))
    print("   Expected: 3")

    print("5. sort then find:", sort_then_find([8, 2, 5, 1], 5))
    print("   Expected: True")


if __name__ == "__main__":
    main()
