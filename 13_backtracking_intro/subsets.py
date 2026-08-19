"""Backtracking practice 1: generate all subsets."""


def subsets(numbers):
    """
    Return every subset of numbers.

    Example:
    subsets([1, 2]) returns [[], [1], [2], [1, 2]]

    Think of each number as a choice:
    - do not include it
    - include it
    """
    result = []
    path = []

    def backtrack(index):
        """
        index: which number we are deciding about now.
        path: the subset currently being built.
        result: all completed subsets.
        """
        # Base case: every number has been decided.
        if index == len(numbers):
            result.append(path.copy())
            return 
        # Choice 1: do not choose numbers[index].
        backtrack(index + 1)

        # Choice 2: choose numbers[index].
        path.append(numbers[index])
        backtrack(index+1)
        # Undo choice 2 before returning to the previous decision.
        path.pop()

    backtrack(0)
    return result


if __name__ == "__main__":
    print(subsets([1, 2, 3]))
    # Expected: [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
