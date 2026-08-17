"""
Minimum Cost Climbing Stairs with dynamic programming.

Core idea:
- Each step has a cost.
- You can climb 1 step or 2 steps at a time.
- Find the minimum cost to reach the top.

Run:
cd "/Users/eden1969/Documents/CS First years/12_dynamic_programming_intro"
python3 min_cost_climbing_stairs.py
"""


def min_cost_climbing_stairs(cost):
    """
    Return the minimum cost to reach the top.

    Example:
    cost = [10, 15, 20]

    You can start at step 0 or step 1.
    Cheapest path:
    - start at step 1, pay 15, climb 2 steps to the top

    Return:
    15

    DP meaning:
    - dp[i] means the minimum cost to reach step i

    Important:
    - the top is step len(cost)
    - top itself has no cost

    Base cases:
    - dp[0] = 0
    - dp[1] = 0

    Transition:
    - dp[i] = min(
        dp[i - 1] + cost[i - 1],
        dp[i - 2] + cost[i - 2]
      )

    Edge cases:
    - if cost is empty, return 0
    - if cost has one step, return 0
    """
    # TODO: write your code here
    if not cost or len(cost) == 1:
        return 0
    
    dp = [0] * (len(cost) + 1)

    dp[0] = 0
    dp[1] = 0

    for i in range(2, len(cost) + 1):
        one_step = dp[i-1] + cost[i-1]
        two_step = dp[i-2] + cost[i-2]
        dp[i] = min(one_step, two_step)

    return dp[len(cost)]

    
    



def min_cost_climbing_stairs_variables(cost):
    """
    Return the minimum cost to reach the top using two variables.

    This is the space-optimized version.
    """
    # TODO: write your code here
    if not cost or len(cost) == 1:
        return 0
    
    prev2 = 0 # dp[i - 2]
    prev1 = 0 # dp[i - 1]

    for i in range(2, len(cost) + 1):
        current = min(prev2 + cost[i-2],
                      prev1 + cost[i-1])
        prev2 = prev1
        prev1 = current
    
    return prev1




def main():
    print(min_cost_climbing_stairs([10, 15, 20]))
    print(min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
    print(min_cost_climbing_stairs([]))
    print(min_cost_climbing_stairs([5]))

    print("\nVariables:")
    print(min_cost_climbing_stairs_variables([10, 15, 20]))
    print(min_cost_climbing_stairs_variables([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
    print(min_cost_climbing_stairs_variables([]))
    print(min_cost_climbing_stairs_variables([5]))

    print("\nExpected:")
    print("15")
    print("6")
    print("0")
    print("0")
    print("15")
    print("6")
    print("0")
    print("0")


if __name__ == "__main__":
    main()
