"""
Minimum size subarray sum.

Core idea:
- Use a variable-size sliding window.
- Expand the right side until the sum is large enough.
- Then shrink the left side to find the shortest valid window.

Run:
cd "/Users/eden1969/Documents/CS First years/11_two_pointers_sliding_window"
python3 minimum_size_subarray_sum.py
"""


def minimum_size_subarray_sum(nums, target):
    """
    Return the minimum length of a continuous subarray
    whose sum is greater than or equal to target.

    Example:
    nums = [2, 3, 1, 2, 4, 3]
    target = 7

    Valid subarrays:
    [2, 3, 1, 2] -> length 4
    [4, 3] -> length 2

    Return:
    2

    Edge cases:
    - if nums is empty, return 0
    - if target <= 0, return 0
    - if no valid subarray exists, return 0

    Hint:
    - left = 0
    - window_sum = 0
    - min_length = float("inf")
    - loop right through nums
    - add nums[right]
    - while window_sum >= target:
        - update min_length
        - remove nums[left]
        - left += 1
    """
    # TODO: write your code here
    if not nums:
        return 0
    if target <= 0:
        return 0
    
    left = 0
    window_sum = 0
    min_length = float("inf")#表示正无穷大

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum >= target:
            current_length = right - left + 1
            min_length = min(min_length, current_length)

            window_sum -= nums[left]
            left += 1
    if min_length == float("inf"):
        return 0
    return min_length


def main():
    print(minimum_size_subarray_sum([2, 3, 1, 2, 4, 3], 7))
    print(minimum_size_subarray_sum([1, 4, 4], 4))
    print(minimum_size_subarray_sum([1, 1, 1, 1], 10))
    print(minimum_size_subarray_sum([], 7))
    print(minimum_size_subarray_sum([1, 2, 3], 0))

    print("\nExpected:")
    print("2")
    print("1")
    print("0")
    print("0")
    print("0")


if __name__ == "__main__":
    main()
