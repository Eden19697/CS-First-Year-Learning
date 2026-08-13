"""
Valid Palindrome with two pointers.

Core idea:
- Use left and right pointers.
- Compare characters from both ends.
- Move both pointers toward the center.

Run:
cd "/Users/eden1969/Documents/CS First years/11_two_pointers_sliding_window"
python3 valid_palindrome.py
"""


def is_palindrome(text):
    """
    Return True if text is a palindrome.
    Otherwise return False.

    Example:
    text = "racecar"
    return True

    text = "hello"
    return False

    Edge cases:
    - empty string returns True
    - one-character string returns True

    Hint:
    - left = 0
    - right = len(text) - 1
    - while left < right:
        - compare text[left] and text[right]
        - if different, return False
        - otherwise move both pointers
    """
    # TODO: write your code here
    if not text:
        return True
    left = 0
    right = len(text) - 1
    
    while left < right:
        if text[left] == text[right]:
            left += 1
            right -= 1
        else:
            return False
    
    return True
    
        
            

    



def main():
    print(is_palindrome("racecar"))
    print(is_palindrome("level"))
    print(is_palindrome("hello"))
    print(is_palindrome(""))
    print(is_palindrome("a"))

    print("\nExpected:")
    print("True")
    print("True")
    print("False")
    print("True")
    print("True")


if __name__ == "__main__":
    main()
