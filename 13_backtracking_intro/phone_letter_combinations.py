"""Backtracking practice 6: phone keypad letter combinations."""


def letter_combinations(digits):
    """
    Return every letter combination represented by phone digits.

    Example:
    letter_combinations("23") returns
    ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    Think before writing:
    - index: which digit are we currently converting?
    - path: letters selected so far
    - phone[digits[index]]: letters available for the current digit
    """
    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    # TODO: if digits is empty, return [].
    if not digits:
        return []
    # TODO: create result and path.
    result = []
    path = []

    # TODO: define backtrack(index).
    # Base case: index == len(digits).
    # Save "".join(path), then return.
    def backtrack(index):
        if index == len(digits):
            result.append("".join(path))
            return

    # Recursive case:
    # - use phone[digits[index]] to get the possible letters
    # - loop through those letters
    # - append one letter, recurse with index + 1, then pop
        letters = phone[digits[index]]
        for i in range(len(letters)):
            path.append(letters[i])
            backtrack(index + 1)
            path.pop() 


    # TODO: call backtrack(0), then return result.
    backtrack(0)
    return result

if __name__ == "__main__":
    print(letter_combinations(""))
    # Expected: []

    print(letter_combinations("2"))
    # Expected: ["a", "b", "c"]

    print(letter_combinations("23"))
    # Expected: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
