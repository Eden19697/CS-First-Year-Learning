"""
Longest substring without repeating characters.

Core idea:
- Use a sliding window.
- The window must not contain duplicate characters.
- Use a set to track characters currently inside the window.

Run:
cd "/Users/eden1969/Documents/CS First years/11_two_pointers_sliding_window"
python3 longest_substring_without_repeat.py
"""


def longest_substring_without_repeat(text):
    """
    Return the length of the longest substring without repeating characters.

    Example:
    text = "abcabcbb"
    return 3

    Because:
    "abc" is the longest substring without repeating characters.

    Edge cases:
    - if text is empty, return 0
    - if text has one character, return 1

    Hint:
    - seen = set()
    - left = 0
    - loop right through text
    - while text[right] is already in seen:
        - remove text[left] from seen
        - left += 1
    - add text[right] to seen
    - update max_length
    """
    # TODO: write your code here
    seen = set()
    left = 0
    max_length = 0
    for right in range(len(text)):
        while text[right] in seen:
            seen.remove(text[left])
            left += 1
        seen.add(text[right])
        if (right-left+1) > max_length:
            max_length = right-left+1
    return max_length

#better version
#current_length = right - left + 1
#max_length = max(max_length, current_length)

def main():
    print(longest_substring_without_repeat("abcabcbb"))
    print(longest_substring_without_repeat("bbbbb"))
    print(longest_substring_without_repeat("pwwkew"))
    print(longest_substring_without_repeat(""))
    print(longest_substring_without_repeat("a"))

    print("\nExpected:")
    print("3")
    print("1")
    print("3")
    print("0")
    print("1")


if __name__ == "__main__":
    main()
