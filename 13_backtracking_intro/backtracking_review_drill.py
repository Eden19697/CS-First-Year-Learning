"""Backtracking review drill.

Rewrite every function from memory. Use your earlier files only after you try.
For every question, first write:
1. What does each recursive parameter mean?
2. What is the base case?
3. What is the choice?
4. What must be undone after recursion?
"""


def subsets(numbers):
    """Return every subset of numbers.

    Example: subsets([1, 2]) -> [[], [2], [1], [1, 2]]

    Hint:
    - index decides whether to select numbers[index]
    - first try not selecting it
    - then append it, recurse, and pop it
    """
    # TODO
    result = []
    path = []

    def backtrack(index):
        if index == len(numbers):
            result.append(path.copy())
            return
        
        backtrack(index + 1)

        path.append(numbers[index])
        backtrack(index + 1)
        path.pop()
    
    backtrack(0)
    return result


def permutations(numbers):
    """Return every ordering of numbers.

    Example: permutations([1, 2]) -> [[1, 2], [2, 1]]

    Hint:
    - path stores the current ordering
    - used[index] says whether numbers[index] is already in path
    - every recursive level loops through all indexes again
    - undo both path and used after recursion
    """
    # TODO
    result = []
    path = []
    used = [False]*len(numbers)

    def backtrack():
        if len(path) == len(numbers):
            result.append(path.copy())
            return
        
        for index in range(len(numbers)):
            if used[index]:
                continue

            path.append(numbers[index])
            used[index] = True

            backtrack()

            path.pop()
            used[index] = False

    backtrack()
    return result


def combination_sum(candidates, target):
    """Return combinations that add up to target; values may be reused.

    Example: combination_sum([2, 3, 6, 7], 7) -> [[2, 2, 3], [7]]

    Hint:
    - recursive parameters: start_index, remaining
    - remaining == 0: save a copy of path
    - remaining < 0: return
    - recurse with the SAME index to allow reuse
    """
    # TODO
    result = []
    path = []

    def backtrack(start_index, remaining):
        if remaining == 0:
            result.append(path.copy())
            return
        if remaining < 0:
            return
        for index in range(start_index, len(candidates)):
            path.append(candidates[index])
            backtrack(index, remaining - candidates[index])
            path.pop()
        
    backtrack(0, target)
    return result


def combination_sum_once(candidates, target):
    """Return combinations that add up to target; each value position is used once.

    Example: combination_sum_once([2, 3, 6, 7], 7) -> [[7]]

    Hint:
    - same structure as combination_sum
    - recurse with index + 1, so this position cannot be used again
    """
    # TODO
    result = []
    path = []

    def backtrack(start_index, remaining):
        if remaining == 0:
            result.append(path.copy())
            return
        if remaining < 0:
            return
        for index in range(start_index, len(candidates)):
            path.append(candidates[index])
            backtrack(index + 1, remaining - candidates[index])
            path.pop()
        
    backtrack(0, target)
    return result


def generate_parentheses(n):
    """Return all valid strings containing n pairs of parentheses.

    Example: generate_parentheses(2) -> ["(())", "()()"]

    Hint:
    - recursive parameters: open_count, close_count
    - add "(" only when open_count < n
    - add ")" only when close_count < open_count
    - complete answer: len(path) == 2 * n
    - save "".join(path)
    """
    # TODO
    result = []
    path = []

    def backtrack(open_count, close_count):
        if len(path) == 2*n:
            result.append("".join(path))
            return
        
        if open_count < n:
            path.append("(")
            backtrack(open_count+1, close_count)
            path.pop()

        if close_count < open_count:
            path.append(")")
            backtrack(open_count, close_count+1)
            path.pop()

    backtrack(0, 0)
    return result

def letter_combinations(digits):
    """Return all phone-keypad letter combinations.

    Example: letter_combinations("23") ->
    ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    Hint:
    - create a phone dict for digits "2" through "9"
    - index means which digit is currently being handled
    - loop through phone[digits[index]]
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
    # TODO
    result = []
    path = []

    def backtrack(index):
        if index == len(digits):
            result.append("".join(path))
            return
        
        for letter in phone[digits[index]]:
            path.append(letter)
            backtrack(index+1)
            path.pop()
    backtrack(0)
    return result


def exists_word(grid, word):
    """Return True if word can be formed using adjacent grid cells.

    A cell cannot be reused on the same path.

    Hint:
    - recursive parameters: row, col, index
    - use a visited set for the CURRENT path
    - check bounds, visited, and character mismatch
    - add before exploring four directions
    - remove before returning from a failed path
    - child True must be returned to the parent
    """
    # TODO
    visited = set()
    rows = len(grid)
    cols = len(grid[0])

    def dfs(row, col, index):
        if index == len(word):
            return True
        if row >= rows or row < 0 or col >= cols or col < 0:
            return False
        if (row, col) in visited:
            return False
        if grid[row][col] != word[index]:
            return False
        
        visited.add((row, col))

        found = (dfs(row + 1, col, index + 1)
                 or dfs(row - 1, col, index + 1)
                 or dfs(row, col+1, index + 1)
                 or dfs(row, col-1, index + 1))
        visited.remove((row, col))
        return found
    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True
    return False

if __name__ == "__main__":
    print("1. subsets")
    print(subsets([1, 2, 3]))
    # Expected: 8 subsets

    print("\n2. permutations")
    print(permutations([1, 2, 3]))
    # Expected: 6 permutations

    print("\n3. combination_sum")
    print(combination_sum([2, 3, 6, 7], 7))
    # Expected: [[2, 2, 3], [7]]

    print("\n4. combination_sum_once")
    print(combination_sum_once([2, 3, 5, 7], 7))
    # Expected: [[2, 5], [7]]

    print("\n5. generate_parentheses")
    print(generate_parentheses(3))
    # Expected: 5 strings

    print("\n6. letter_combinations")
    print(letter_combinations("23"))
    # Expected: 9 strings

    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    print("\n7. exists_word")
    print(exists_word(board, "ABCCED"))  # Expected: True
    print(exists_word(board, "SEE"))     # Expected: True
    print(exists_word(board, "ABCB"))    # Expected: False
