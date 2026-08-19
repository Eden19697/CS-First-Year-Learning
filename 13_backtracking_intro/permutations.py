"""Backtracking practice 2: generate all permutations."""


def permutations(numbers):
    """
    Return every ordering of numbers.

    Example:
    permutations([1, 2]) returns [[1, 2], [2, 1]]

    Difference from subsets:
    - subsets: each number can be selected or skipped
    - permutations: every number must be selected exactly once

    Think before writing:
    - path: the ordering currently being built
    - used[i]: whether numbers[i] is already in path
    - base case: len(path) == len(numbers)
    """
    # TODO: create result, path, and used.
    result = []
    path = []
    used = [False] * len(numbers)
    
    # TODO: define backtrack().
    def backtrack():
    # Base case:
    # - when path contains every number, append path.copy() to result.
        if len(path) == len(numbers):
            result.append(path.copy())
            return
    # Recursive case:
    # - loop through every index in numbers
        for index in range(len(numbers)):
            if used[index]:
                continue
    # - skip it if used[index] is True
    # - otherwise: choose it, mark used[index], recurse,
            path.append(numbers[index])
            used[index] = True

            backtrack()
    #   then undo both choices (pop and mark unused).
            path.pop()
            used[index] = False

    # TODO: call backtrack(), then return result.
    backtrack()
    return result


if __name__ == "__main__":
    print(permutations([]))
    print(permutations([1]))
    print(permutations([1, 2]))
    print(permutations([1, 2, 3]))
    # Expected for [1, 2]: [[1, 2], [2, 1]]
