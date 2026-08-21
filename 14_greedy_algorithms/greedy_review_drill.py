"""Greedy review drill.

Rewrite each function from memory before reopening the earlier practice files.
For every question, first write one sentence explaining the greedy choice.
"""


def max_non_overlapping_intervals(intervals):
    """Return the largest number of non-overlapping intervals.

    Greedy choice: select the available interval that ends earliest.
    Example: [(1, 3), (2, 4), (3, 5), (5, 7), (8, 9)] -> 4
    """
    # TODO: handle empty input
    # TODO: sort by interval end
    # TODO: track last_end and count selected intervals
    if not intervals:
        return 0
    new = sorted(intervals, key= lambda interval:interval[1])
    count = 0
    last_end = float("-inf")
    for obj in new:
        if obj[0] >= last_end:
            count += 1
            last_end = obj[1]
    return count


def greedy_coin_change(coins, amount):
    """Return a greedy coin choice, always using the largest available coin.

    Example: [1, 5, 10, 25], 41 -> [25, 10, 5, 1]
    Reminder: this is not always the minimum number of coins.
    """
    # TODO: sort from largest to smallest
    result = []
    # TODO: repeatedly use a coin while it does not exceed amount
    sorted_list = sorted(coins, reverse=True)
    for coin in sorted_list:
        while amount-coin >= 0:
            amount -= coin
            result.append(coin)
    return result

def find_content_children(greed, cookies):
    """Return the maximum number of children that can be satisfied.

    Greedy choice: use the smallest suitable cookie for the least demanding child.
    Example: [1, 2, 3], [1, 1] -> 1
    """
    # TODO: sort both lists
    sorted_greed = sorted(greed)
    sorted_cookie = sorted(cookies)
    index_cookie = 0
    index_greed = 0
    # TODO: use child_index and cookie_index
    while index_cookie < len(sorted_cookie) and index_greed < len(sorted_greed):
        if sorted_cookie[index_cookie] >= sorted_greed[index_greed]:
            index_greed += 1
        index_cookie += 1
    return index_greed

    


def can_jump(numbers):
    """Return True if the final index is reachable.

    Greedy state: farthest is the furthest index reachable so far.
    Example: [2, 3, 1, 1, 4] -> True
    Example: [3, 2, 1, 0, 4] -> False
    """
    # TODO: loop with enumerate
    # TODO: fail when index > farthest
    farthest = 0
    # TODO: update farthest with max(farthest, index + jump_length)
    for index, jump_length in enumerate(numbers):
        if index > farthest:
            return False
        farthest = max(farthest, index + jump_length)
    return True


def minimum_arrows(intervals):
    """Return the minimum arrows needed to hit every interval.

    Greedy choice: shoot at the earliest available ending position.
    Example: [(10, 16), (2, 8), (1, 6), (7, 12)] -> 2
    """
    # TODO: handle empty input
    # TODO: sort by end position
    # TODO: track arrows and current_arrow_position
    if not intervals:
        return 0
    arrow = 1
    sorted_list = sorted(intervals, key = lambda interval:interval[1])
    last_end = sorted_list[0][1]
    
    for obj in sorted_list:
        if obj[0] > last_end:
            arrow += 1
            last_end = obj[1]
    return arrow


def partition_labels(text):
    """Return the lengths of the maximum valid string partitions.

    Greedy state: end is the furthest final occurrence required by this partition.
    Example: "ababcbacadefegdehijhklij" -> [9, 7, 8]
    """
    # TODO: build a dict of final indexes
    # TODO: scan text while updating the current end boundary
    # TODO: cut a partition when index == end
    if not text:
        return []
    save = {}
    for index, char in enumerate(text):
        save[char] = index

    result = []
    start = 0
    end = 0

    for i, char in enumerate(text):
        end = max(end, save[char])

        if i == end:
            result.append(i - start + 1)
            start = i + 1

    return result




def max_profit(prices):
    """Return the best profit from buying once and selling later.

    Greedy state: lowest_price is the lowest price seen so far.
    Example: [7, 1, 5, 3, 6, 4] -> 5
    """
    # TODO: handle empty input
    # TODO: track lowest_price and best_profit
    if not prices:
        return 0
    lowest_price = prices[0]
    best_profit = 0

    for i in range(1, len(prices)):
        current = prices[i]
        if current < lowest_price:
            lowest_price = current
        else:
            best_profit = max(best_profit, current-lowest_price)
    return best_profit


if __name__ == "__main__":
    print("1. interval scheduling")
    print(max_non_overlapping_intervals([(1, 3), (2, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]))
    # Expected: 4

    print("\n2. greedy coin change")
    print(greedy_coin_change([1, 5, 10, 25], 41))
    # Expected: [25, 10, 5, 1]

    print("\n3. assign cookies")
    print(find_content_children([1, 2, 3], [1, 1]))
    # Expected: 1

    print("\n4. jump game")
    print(can_jump([2, 3, 1, 1, 4]))
    print(can_jump([3, 2, 1, 0, 4]))
    # Expected: True, False

    print("\n5. minimum arrows")
    print(minimum_arrows([(10, 16), (2, 8), (1, 6), (7, 12)]))
    # Expected: 2

    print("\n6. partition labels")
    print(partition_labels("ababcbacadefegdehijhklij"))
    # Expected: [9, 7, 8]

    print("\n7. best time to buy and sell stock")
    print(max_profit([7, 1, 5, 3, 6, 4]))
    # Expected: 5
