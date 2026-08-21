"""Greedy practice 2: greedy coin change and its limitation."""


def greedy_coin_change(coins, amount):
    """
    Return one greedy choice of coins, taking the largest possible coin first.

    Example:
    greedy_coin_change([1, 5, 10, 25], 41) returns [25, 10, 5, 1].

    Important:
    This does NOT always return the fewest coins for arbitrary coin systems.
    For coins [1, 3, 4] and amount 6:
    - greedy chooses [4, 1, 1] (3 coins)
    - the best answer is [3, 3] (2 coins)

    This function demonstrates why a greedy rule needs proof before we trust it.
    """
    # TODO: return [] for amount == 0.
    # TODO: sort coins from largest to smallest.
    # TODO: for every coin, choose it repeatedly while it does not exceed amount.
    # TODO: subtract the chosen coin from amount and append it to result.
    # TODO: return result when amount reaches 0.
    # Optional: decide what to return when amount cannot be formed exactly.
    if amount == 0:
        return []
    
    result = []
    sorted_coins = sorted(coins, reverse=True)

    for coin in sorted_coins:
        while coin <= amount:
            amount -= coin
            result.append(coin)

    return result

        
        

    


if __name__ == "__main__":
    print(greedy_coin_change([1, 5, 10, 25], 41))
    # Expected: [25, 10, 5, 1]

    print(greedy_coin_change([1, 3, 4], 6))
    # Greedy output: [4, 1, 1]
    # Best possible output from DP: [3, 3]
