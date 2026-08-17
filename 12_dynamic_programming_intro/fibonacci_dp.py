"""
Fibonacci with recursion and dynamic programming.

Core idea:
- Recursion solves the problem by calling itself.
- Dynamic programming saves previous answers to avoid repeated work.

Run:
cd "/Users/eden1969/Documents/CS First years/12_dynamic_programming_intro"
python3 fibonacci_dp.py
"""


def fibonacci_recursive(n):
    """
    Return the nth Fibonacci number using plain recursion.

    Fibonacci:
    fib(0) = 0
    fib(1) = 1
    fib(n) = fib(n - 1) + fib(n - 2)

    Base cases:
    - n == 0 -> 0
    - n == 1 -> 1

    Recursive case:
    - fib(n - 1) + fib(n - 2)

    Edge case:
    - if n < 0, return None
    """
    # TODO: write your code here
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

    


def fibonacci_dp_list(n):
    """
    Return the nth Fibonacci number using a DP list.

    dp[i] means:
    - the ith Fibonacci number

    Transition:
    - dp[i] = dp[i - 1] + dp[i - 2]

    Edge case:
    - if n < 0, return None
    """
    # TODO: write your code here
    if n< 0:
        return None
    
    dp = [0,1]

    for i in range(2,n+1):
        dp.append(dp[i-1]+dp[i-2])
    
    return dp[n]
    
    


def fibonacci_dp_variables(n):
    """
    Return the nth Fibonacci number using two variables.

    This is the space-optimized DP version.

    Instead of storing the whole dp list, keep only:
    - previous previous value
    - previous value

    Edge case:
    - if n < 0, return None
    """
    # TODO: write your code here
    if n < 0:
        return None
    if n == 0:
        return 0

    if n == 1:
        return 1
    
    prev2 = 0
    prev1 = 1

    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1



def main():
    print("Recursive:")
    print(fibonacci_recursive(0))
    print(fibonacci_recursive(1))
    print(fibonacci_recursive(6))

    print("\nDP list:")
    print(fibonacci_dp_list(0))
    print(fibonacci_dp_list(1))
    print(fibonacci_dp_list(6))

    print("\nDP variables:")
    print(fibonacci_dp_variables(0))
    print(fibonacci_dp_variables(1))
    print(fibonacci_dp_variables(6))
    print(fibonacci_dp_variables(-1))

    print("\nExpected:")
    print("0")
    print("1")
    print("8")
    print("0")
    print("1")
    print("8")
    print("0")
    print("1")
    print("8")
    print("None")


if __name__ == "__main__":
    main()
