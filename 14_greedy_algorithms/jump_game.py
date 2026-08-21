"""Greedy practice 4: determine whether the last index is reachable."""


def can_jump(numbers):
    """
    Return True if it is possible to reach the final index.

    numbers[index] is the maximum jump length from index.

    Examples:
    can_jump([2, 3, 1, 1, 4]) returns True.
    One possible route is index 0 -> index 1 -> index 4.

    can_jump([3, 2, 1, 0, 4]) returns False.
    Index 3 blocks every possible route to index 4.

    Greedy state:
    - farthest: the furthest index reachable so far
    """
    # An empty list needs no jumps, so the final position is vacuously reachable.
    if not numbers:
        return True
    # TODO: set farthest = 0.
    farthest = 0
    # TODO: loop through each index and jump length.
    # - if index > farthest, this index cannot be reached; return False
    # - otherwise, update farthest using max(farthest, index + jump_length)
    for index, jump_length in enumerate(numbers):
        if index > farthest:
            return False
        farthest = max(farthest, index + jump_length)

    # TODO: return True after the loop finishes.
    return True


if __name__ == "__main__":
    print(can_jump([]))              # Expected: True
    print(can_jump([0]))             # Expected: True
    print(can_jump([2, 3, 1, 1, 4])) # Expected: True
    print(can_jump([3, 2, 1, 0, 4])) # Expected: False
