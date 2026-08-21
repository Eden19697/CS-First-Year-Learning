"""Greedy practice 1: select the maximum number of non-overlapping intervals."""


def max_non_overlapping_intervals(intervals):
    """
    Return the largest number of intervals that do not overlap.

    Each interval is a tuple: (start, end).
    An interval may start exactly when the previous one ends.

    Example:
    [(1, 3), (2, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
    returns 4: (1, 3), (3, 5), (5, 7), (8, 9)

    Greedy idea:
    Choose the available interval that ends earliest.
    It leaves the most time available for future intervals.
    """
    # TODO: return 0 when intervals is empty.
    if not intervals:
        return 0
    # TODO: sort intervals by their end time.
    # Hint: sorted(intervals, key=lambda interval: interval[1])
    sorted_intervals = sorted(intervals, key=lambda interval: interval[1])
    # TODO: create count and last_end.
    # last_end means: when does the most recently selected interval end?
    count = 0
    last_end = float("-inf")

    # TODO: loop through sorted intervals.
    # If start >= last_end, select this interval:
    # - add 1 to count
    # - update last_end to end
    for start, end in sorted_intervals:
        if start >= last_end:
            count += 1
            last_end = end

    # TODO: return count.
    return count


if __name__ == "__main__":
    print(max_non_overlapping_intervals([]))
    # Expected: 0

    print(max_non_overlapping_intervals([(1, 3), (2, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]))
    # Expected: 4

    print(max_non_overlapping_intervals([(1, 2), (2, 3), (3, 4)]))
    # Expected: 3
