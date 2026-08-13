"""
Two Pointers / Sliding Window review drill.

Goal:
- Rewrite the core templates from memory.
- Practice choosing the right pointer pattern from the problem.

Run:
cd "/Users/eden1969/Documents/CS First years/11_two_pointers_sliding_window"
python3 review_drill.py
"""


def two_sum_sorted(nums, target):
    """
    Pattern:
    - left/right pointers
    - sorted array

    Return indices of two numbers whose sum is target.
    If no pair exists, return [].
    """
    # TODO: write your code here
    if not nums:
        return []
    if len(nums) < 2:
        return []
    
    left = 0
    right = len(nums) -1

    while left < right :
        total = nums[left] + nums[right]

        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []




def is_palindrome(text):
    """
    Pattern:
    - left/right pointers
    - compare both ends

    Return True if text is a palindrome.
    Otherwise return False.
    """
    # TODO: write your code here
    if not text:
        return True
    left = 0
    right = len(text)-1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1

    return True



def max_sum_subarray_k(nums, k):
    """
    Pattern:
    - fixed-size sliding window

    Return the maximum sum of any continuous subarray of size k.
    If k is invalid, return 0.
    """
    # TODO: write your code here
    if not nums:
        return 0
    if k > len(nums) or k < 0:
        return 0
    
    window_sum = 0
    max_sum = None

    for right in range(len(nums)):
        window_sum += nums[right]
        if right >= k-1:
            if max_sum is None or window_sum > max_sum:
                max_sum = window_sum
            
            left = right -k +1
            window_sum -= nums[left]
    return max_sum


def longest_substring_without_repeat(text):
    """
    Pattern:
    - variable-size sliding window
    - set to track characters in the current window

    Return the length of the longest substring without repeating characters.
    """
    # TODO: write your code here
    if not text:
        return 0
    
    slow = 0
    seen = set()
    max_length = 0

    for fast in range(len(text)):
        while text[fast] in seen:
            seen.remove(text[slow])
            slow += 1

        seen.add(text[fast])
        if (fast-slow+1) > max_length:
            max_length = fast-slow+1
    return max_length


def main():
    print("two_sum_sorted:")
    print(two_sum_sorted([1, 2, 3, 4, 6], 6))
    print(two_sum_sorted([1, 2, 3], 10))

    print("\nis_palindrome:")
    print(is_palindrome("racecar"))
    print(is_palindrome("hello"))

    print("\nmax_sum_subarray_k:")
    print(max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3))
    print(max_sum_subarray_k([1, 2], 3))

    print("\nlongest_substring_without_repeat:")
    print(longest_substring_without_repeat("abcabcbb"))
    print(longest_substring_without_repeat("bbbbb"))

    print("\nExpected:")
    print("[1, 3]")
    print("[]")
    print("True")
    print("False")
    print("9")
    print("0")
    print("3")
    print("1")


if __name__ == "__main__":
    main()
