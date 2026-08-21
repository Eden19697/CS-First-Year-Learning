"""Greedy practice 7: maximum profit from one stock transaction."""


def max_profit(prices):
    """
    Return the largest profit from buying once and selling once later.

    A purchase must happen before its sale.
    Return 0 when no profit is possible.

    Example:
    max_profit([7, 1, 5, 3, 6, 4]) returns 5.
    Buy at 1 and sell later at 6.

    Greedy state:
    - lowest_price: the lowest price seen before or on today
    - best_profit: the greatest valid profit seen so far
    """
    # TODO: return 0 for an empty price list.
    if not prices:
        return 0
    # TODO: set lowest_price to the first price.
    lowest_price = prices[0]
    # TODO: set best_profit to 0.
    best_profit = 0

    # TODO: loop through every later price.
    # - update lowest_price if today's price is lower
    # - otherwise, calculate today's possible profit:
    #   current_price - lowest_price
    # - update best_profit if that profit is larger
    for i in range(1,len(prices)):
        current = prices[i]
        if current < lowest_price:
            lowest_price = current
        else:
            best_profit = max(best_profit, current - lowest_price)

    return best_profit

    # TODO: return best_profit.
    


if __name__ == "__main__":
    print(max_profit([]))
    # Expected: 0

    print(max_profit([7, 1, 5, 3, 6, 4]))
    # Expected: 5

    print(max_profit([7, 6, 4, 3, 1]))
    # Expected: 0
