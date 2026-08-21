"""Greedy practice 5: minimum arrows needed to burst every balloon."""


def minimum_arrows(intervals):
    """
    Return the minimum number of arrows needed to hit all intervals.

    An arrow shot at position x hits every interval where start <= x <= end.

    Example:
    [(10, 16), (2, 8), (1, 6), (7, 12)] returns 2.
    - Shoot one arrow at 6: hits (1, 6) and (2, 8)
    - Shoot one arrow at 12: hits (7, 12) and (10, 16)

    Greedy idea:
    Sort intervals by ending position. Shoot the current arrow at the earliest
    ending position. Keep using that arrow while later intervals still contain it.
    """
    # TODO: return 0 for an empty list.
    if not intervals:
        return 0
    # TODO: sort intervals by end position.
    sorted_intervals = sorted(intervals, key = lambda interval:interval[1])
    # TODO: start with one arrow at the end of the first sorted interval.
    arrow = 1
    current_arrow_position = sorted_intervals[0][1]
    # TODO: loop through the remaining intervals:
    # - if start > current_arrow_position, the current arrow cannot hit it
    #   so add another arrow and set its position to this interval's end
    # - otherwise, the current arrow already hits this interval
    for obj in sorted_intervals:
        if obj[0] > current_arrow_position:
            arrow += 1
            current_arrow_position = obj[1]

    # TODO: return the arrow count.
    return arrow


if __name__ == "__main__":
    print(minimum_arrows([]))
    # Expected: 0

    print(minimum_arrows([(10, 16), (2, 8), (1, 6), (7, 12)]))
    # Expected: 2

    print(minimum_arrows([(1, 2), (2, 3), (3, 4), (4, 5)]))
    # Expected: 2
