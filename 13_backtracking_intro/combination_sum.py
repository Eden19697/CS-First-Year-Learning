"""Backtracking practice 3: find combinations that add up to a target."""


def combination_sum(candidates, target):
    """
    Return all combinations of candidates that add up to target.

    A candidate may be used more than once.
    The order inside a combination does not matter:
    [2, 3, 3] and [3, 2, 3] are the same answer, so return only one of them.

    Example:
    combination_sum([2, 3, 6, 7], 7)
    returns [[2, 2, 3], [7]]

    Think before writing:
    - path: numbers selected on this route
    - remaining: how much is still needed to reach target
    - start_index: where the next choice may start
    """
    # TODO: create result and path.
    result = []
    path = []

    # TODO: define backtrack(start_index, remaining).
    def backtrack(start_index, remaining):
    # Base case 1: remaining == 0
        if remaining == 0:
    # - path is a complete answer; save path.copy().
            result.append(path.copy())
    # Base case 2: remaining < 0
        if remaining < 0:
    # - this path has gone too far; return.
            return

    # Recursive case:
    # - loop from start_index through candidates.
        for index in range(start_index, len(candidates)):
    # - choose candidates[index] by appending it to path.
            path.append(candidates[index])
    # - recurse with the SAME index, because the current number may be reused.
    # - reduce remaining by candidates[index].
            backtrack(index, remaining - candidates[index])
    # - pop to undo the choice.
            path.pop()
    # TODO: start with backtrack(0, target), then return result.
    backtrack(0,target)
    return result


if __name__ == "__main__":
    print(combination_sum([2, 3, 6, 7], 7))
    # Expected: [[2, 2, 3], [7]]

    print(combination_sum([2, 3, 5], 8))
    # Expected: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
