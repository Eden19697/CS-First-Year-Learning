"""Backtracking practice: rewrite subsets without looking at the solution."""


def subsets(numbers):
    """
    Return every subset of numbers.

    Examples:
    subsets([]) returns [[]]
    subsets([1, 2]) returns [[], [2], [1], [1, 2]]

    Before writing code, say this out loud:
    - index means: which number am I deciding about?
    - path means: which numbers have I selected on this route?
    - each number has two choices: do not choose it / choose it
    """
    # 1. Create result and path.
    result = []
    path = []

    # 2. Define backtrack(index).
    #    Base case: index == len(numbers).
    #    Save a COPY of path, then return.
    def backtrack(index):
        if index == len(numbers):
            result.append(path.copy())
            return

    # 3. First recursive branch: do not choose numbers[index].
        backtrack(index + 1)
    # 4. Second recursive branch: append numbers[index], recurse,
        path.append(numbers[index])
        backtrack(index + 1)
    #    then pop it to undo this choice.
        path.pop()

    # 5. Start with backtrack(0), then return result.
    backtrack(0)
    return result


if __name__ == "__main__":
    print(subsets([]))
    print(subsets([1]))
    print(subsets([1, 2]))
    print(subsets([1, 2, 3]))
