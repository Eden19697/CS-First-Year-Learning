"""Big-O examples.

Run:
python3 big_o_examples.py

Before reading each complexity comment, first predict:
1. Time complexity (worst case)
2. Extra space complexity
3. Which line or loop causes that cost
"""


def find_first_even(numbers):
    """Return the first even number, or None.

    Time: O(n) in the worst case.
    Extra space: O(1).
    """
    for number in numbers:
        if number % 2 == 0:
            return number
    return None


def contains_duplicate_with_set(numbers):
    """Return whether numbers contains a duplicate.

    Time: O(n) on average: each set lookup/add is O(1) on average.
    Extra space: O(n): seen may store every number.
    """
    seen = set()

    for number in numbers:
        if number in seen:
            return True
        seen.add(number)

    return False


def has_duplicate_after_sorting(numbers):
    """Return whether numbers contains a duplicate by sorting first.

    Time: O(n log n) + O(n), which simplifies to O(n log n).
    Extra space: O(n), because sorted returns a new list.
    """
    sorted_numbers = sorted(numbers)

    for index in range(1, len(sorted_numbers)):
        if sorted_numbers[index] == sorted_numbers[index - 1]:
            return True

    return False


def binary_search(numbers, target):
    """Return target's index in a sorted list, or -1 if it is absent.

    Time: O(log n): each loop discards about half the search range.
    Extra space: O(1).
    """
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def count_unique_pairs(numbers):
    """Return how many index pairs exist.

    Time: O(n^2): the inner loop runs once for many outer-loop values.
    Extra space: O(1).
    """
    count = 0

    for left in range(len(numbers)):
        for right in range(left + 1, len(numbers)):
            count += 1

    return count


def binary_search_for_each_number(numbers, target):
    """Search a sorted list once for every element.

    Time: O(n log n): n outer iterations, each doing O(log n) work.
    Extra space: O(1).
    """
    searches = 0

    for _ in numbers:
        binary_search(numbers, target)
        searches += 1

    return searches


def main():
    numbers = [7, 3, 5, 3, 2]
    sorted_numbers = [1, 3, 5, 7, 9, 11, 13]

    print("first even:", find_first_even(numbers))
    print("duplicate with set:", contains_duplicate_with_set(numbers))
    print("duplicate after sorting:", has_duplicate_after_sorting(numbers))
    print("binary search for 9:", binary_search(sorted_numbers, 9))
    print("unique pairs:", count_unique_pairs(numbers))
    print("repeated binary searches:", binary_search_for_each_number(sorted_numbers, 9))


if __name__ == "__main__":
    main()
