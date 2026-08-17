"""
Coin Change Intro with dynamic programming.

Core idea:
- Given coin values and an amount.
- Find the minimum number of coins needed to make that amount.
- Each coin can be used multiple times.

Run:
cd "/Users/eden1969/Documents/CS First years/12_dynamic_programming_intro"
python3 coin_change_intro.py
"""


def coin_change(coins, amount):
    """
    Return the minimum number of coins needed to make amount.

    Example:
    coins = [1, 2, 5]
    amount = 11

    Best:
    5 + 5 + 1

    Return:
    3

    DP meaning:
    - dp[i] means the minimum number of coins needed to make amount i

    Base case:
    - dp[0] = 0

    Transition:
    - for each i from 1 to amount:
        - for each coin:
            - if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    Edge cases:
    - if amount < 0, return -1
    - if amount == 0, return 0
    - if no combination works, return -1
    """
    # TODO: write your code here
    if amount < 0:
        return -1
    if amount == 0:
        return 0
    
    dp = [float("inf")]*(amount+1)
    dp[0] = 0

    for i in range(1, amount+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[amount] == float("inf"):
        return -1
    return dp[amount]
    



def main():
    print(coin_change([1, 2, 5], 11))
    print(coin_change([2], 3))
    print(coin_change([1], 0))
    print(coin_change([1, 3, 4], 6))

    print("\nExpected:")
    print("3")
    print("-1")
    print("0")
    print("2")


if __name__ == "__main__":
    main()
