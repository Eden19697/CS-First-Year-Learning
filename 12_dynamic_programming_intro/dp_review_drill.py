"""
Dynamic Programming review drill.

Goal:
- Practice defining dp[i].
- Practice writing base cases.
- Practice writing transitions.
- Practice converting repeated subproblems into a DP table.

Run:
cd "/Users/eden1969/Documents/CS First years/12_dynamic_programming_intro"
python3 dp_review_drill.py
"""


def fibonacci(n):
    """
    dp[i] means:
    - the ith Fibonacci number

    Transition:
    - dp[i] = dp[i - 1] + dp[i - 2]
    """
    # TODO: write your code here
    if n < 0:
        return None
    dp = [0, 1]

    for i in range(2,n+1):
        current = dp[i-1] + dp[i-2]
        dp.append(current)

    return dp[n] 


def climb_stairs(n):
    """
    dp[i] means:
    - number of ways to reach step i

    Transition:
    - dp[i] = dp[i - 1] + dp[i - 2]
    """
    # TODO: write your code here
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    prev2 = 1
    prev1 = 1

    for i in range(2, n+1):
        total = prev1 + prev2
        prev1 = prev2
        prev2 = total
    return prev2


def min_cost_climbing_stairs(cost):
    """
    dp[i] means:
    - minimum cost to reach step i

    Transition:
    - dp[i] = min(
        dp[i - 1] + cost[i - 1],
        dp[i - 2] + cost[i - 2]
      )
    """
    # TODO: write your code here
    if not cost or len(cost) == 1:
        return 0
    
    dp = [0] * (len(cost)+1)
    
    for i in range(2, len(cost)+1):
        one = dp[i-1] + cost[i-1]
        two = dp[i-2] + cost[i-2]
        dp[i] = min(one, two)

    return dp[len(cost)]



def house_robber(nums):
    """
    dp[i] means:
    - maximum money from the first i houses

    Transition:
    - dp[i] = max(
        dp[i - 1],
        dp[i - 2] + nums[i - 1]
      )
    """
    # TODO: write your code here
    if not nums:
        return 0
    
    prev2 = nums[0]
    prev1 = 0

    for i in range(2, len(nums)+1):
        rob_current = prev1 + nums[i-1]
        skip_current = prev2
        current = max(rob_current,skip_current)
        prev1 = prev2
        prev2 = current
    return prev2


def coin_change(coins, amount):
    """
    dp[i] means:
    - minimum number of coins needed to make amount i

    Transition:
    - dp[i] = min(dp[i], dp[i - coin] + 1)
    """
    # TODO: write your code here
    if amount < 0:
        return -1
    if amount == 0:
        return 0
    
    dp = [float("inf")] * (amount+1)

    dp[0] = 0
    
    for i in range(1, amount+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[amount] == float("inf"):
        return -1
    return dp[amount]

def main():
    print("fibonacci:", fibonacci(6))
    print("climb_stairs:", climb_stairs(5))
    print("min_cost:", min_cost_climbing_stairs([10, 15, 20]))
    print("house_robber:", house_robber([2, 1, 1, 2]))
    print("coin_change:", coin_change([1, 2, 5], 11))

    print("\nExpected:")
    print("fibonacci: 8")
    print("climb_stairs: 8")
    print("min_cost: 15")
    print("house_robber: 4")
    print("coin_change: 3")


if __name__ == "__main__":
    main()
