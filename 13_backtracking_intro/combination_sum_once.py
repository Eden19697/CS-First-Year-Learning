"""Backtracking practice 4: combinations where each number is used at most once."""


def combination_sum_once(candidates, target):
    """
    Return combinations that add up to target.

    Each list position can be used at most once.

    Example:
    combination_sum_once([2, 3, 6, 7], 7) returns [[7]].
    It must NOT return [2, 2, 3], because there is only one 2.

    Main difference from combination_sum:
    - combination_sum: recurse with index, so the chosen value may be reused
    - this problem: recurse with index + 1, so the chosen position cannot be reused
    """
    # TODO: create result and path.
    result = []
    path = []

    # TODO: define backtrack(start_index, remaining).
    # - if remaining == 0, save path.copy() and return
    # - if remaining < 0, return
    def backtrack(start_index, remaining):
        if remaining == 0:
            result.append(path.copy())
            return
        if remaining < 0:
            return
    # TODO: loop from start_index through candidates.
    # - append candidates[index]
    # - recurse with index + 1 and the reduced remaining
    # - pop to undo the choice
        for index in range(start_index, len(candidates)):
            path.append(candidates[index])
            backtrack(index + 1, remaining - candidates[index])
            path.pop()
    # TODO: call backtrack(0, target), then return result.
    backtrack(0, target)
    return result


if __name__ == "__main__":
    print(combination_sum_once([2, 3, 6, 7], 7))
    # Expected: [[7]]

    print(combination_sum_once([2, 3, 5, 7], 7))
    # Expected: [[2, 5], [7]]
