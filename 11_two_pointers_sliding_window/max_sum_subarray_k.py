"""
Maximum sum of a subarray with fixed size k.

Core idea:
- Use a sliding window of size k.
- Add the new right value into window_sum.
- Once the window reaches size k:
  - update max_sum
  - remove the leftmost value before moving on

Run:
cd "/Users/eden1969/Documents/CS First years/11_two_pointers_sliding_window"
python3 max_sum_subarray_k.py
"""


def max_sum_subarray_k(nums, k):
    """
    Return the maximum sum of any continuous subarray of size k.

    Example:
    nums = [2, 1, 5, 1, 3, 2]
    k = 3

    Subarrays of size 3:
    [2, 1, 5] -> 8
    [1, 5, 1] -> 7
    [5, 1, 3] -> 9
    [1, 3, 2] -> 6

    Return:
    9

    Edge cases:
    - if k <= 0, return 0
    - if k > len(nums), return 0
    - if nums is empty, return 0

    Hint:
    - window_sum = 0
    - max_sum = None
    - loop right through nums
    - add nums[right]
    - when right >= k - 1:
        - update max_sum
        - remove nums[right - k + 1]
    """
    # TODO: write your code here
    if k <= 0:
        return 0
    
    if k > len(nums):
        return 0
    
    if not nums:
        return 0
    
    window_sum = 0
    max_sum = None

    for right in range(len(nums)):
        window_sum += nums[right]

        if right >= k-1:
            if max_sum is None or window_sum > max_sum:
                max_sum = window_sum

            left = right - k + 1
            window_sum -= nums[left]
    return max_sum



def main():
    print(max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3))
    print(max_sum_subarray_k([1, 2, 3, 4], 2))
    print(max_sum_subarray_k([5], 1))
    print(max_sum_subarray_k([], 3))
    print(max_sum_subarray_k([1, 2], 3))

    print("\nExpected:")
    print("9")
    print("7")
    print("5")
    print("0")
    print("0")


if __name__ == "__main__":
    main()
