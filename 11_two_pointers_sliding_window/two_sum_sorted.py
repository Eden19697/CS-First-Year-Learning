"""
Two Sum in a sorted array.

Core idea:
- Use two pointers: left and right.
- Because the list is sorted:
  - if nums[left] + nums[right] is too small, move left rightward
  - if nums[left] + nums[right] is too large, move right leftward

Run:
cd "/Users/eden1969/Documents/CS First years/11_two_pointers_sliding_window"
python3 two_sum_sorted.py
"""


def two_sum_sorted(nums, target):
    """
    Return the indices of two numbers whose sum is target.

    Example:
    nums = [1, 2, 3, 4, 6]
    target = 6
    return [1, 3]

    Because:
    nums[1] + nums[3] = 2 + 4 = 6

    Edge cases:
    - if no pair exists, return []
    - if nums has fewer than 2 numbers, return []

    Hint:
    - left = 0
    - right = len(nums) - 1
    - while left < right
    """
    # TODO: write your code here
    if len(nums) < 2:
        return []
    left = 0
    right = len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            return [left,right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []



def main():
    print(two_sum_sorted([1, 2, 3, 4, 6], 6))
    print(two_sum_sorted([2, 5, 9, 11], 14))
    print(two_sum_sorted([1, 2, 3], 10))
    print(two_sum_sorted([], 5))

    print("\nExpected:")
    print("[1, 3]")
    print("[1, 2]")
    print("[]")
    print("[]")


if __name__ == "__main__":
    main()
