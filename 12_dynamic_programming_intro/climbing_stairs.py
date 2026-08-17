"""
Climbing Stairs with dynamic programming.

Core idea:
- You can climb 1 step or 2 steps at a time.
- Count how many different ways there are to reach step n.

Run:
cd "/Users/eden1969/Documents/CS First years/12_dynamic_programming_intro"
python3 climbing_stairs.py
"""


def climb_stairs(n):
    """
    Return how many ways to climb to the top.

    Example:
    n = 3

    Ways:
    1 + 1 + 1
    1 + 2
    2 + 1

    Return:
    3

    DP meaning:
    - dp[i] means how many ways to reach step i

    Base cases:
    - dp[0] = 1
    - dp[1] = 1

    Transition:
    - dp[i] = dp[i - 1] + dp[i - 2]

    Edge cases:
    - if n < 0, return 0
    """
    # TODO: write your code here
    if n < 0:
        return 0
    
    dp = [1,1]

    for i in range(2,n+1):
        dp.append(dp[i-1]+dp[i-2])
    
    return dp[n]


def climb_stairs_variables(n):
    """
    Return how many ways to climb to the top using two variables.

    This is the space-optimized version.
    """
    # TODO: write your code here
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    prev2 = 1
    prev1 = 1

    for i in range(2, n+1):
        total = prev2 + prev1
        prev1 = prev2
        prev2 = total
    return prev2

def main():
    print(climb_stairs(0))
    print(climb_stairs(1))
    print(climb_stairs(2))
    print(climb_stairs(3))
    print(climb_stairs(5))
    print(climb_stairs(-1))

    print("\nVariables:")
    print(climb_stairs_variables(0))
    print(climb_stairs_variables(1))
    print(climb_stairs_variables(2))
    print(climb_stairs_variables(3))
    print(climb_stairs_variables(5))
    print(climb_stairs_variables(-1))

    print("\nExpected:")
    print("1")
    print("1")
    print("2")
    print("3")
    print("8")
    print("0")
    print("1")
    print("1")
    print("2")
    print("3")
    print("8")
    print("0")


if __name__ == "__main__":
    main()
