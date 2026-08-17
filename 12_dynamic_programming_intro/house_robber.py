"""
House Robber with dynamic programming.

Core idea:
- You cannot rob two adjacent houses.
- For each house, choose:
  - skip it
  - rob it

Run:
cd "/Users/eden1969/Documents/CS First years/12_dynamic_programming_intro"
python3 house_robber.py
"""


def rob(nums):
    """
    Return the maximum amount of money you can rob.

    Example:
    nums = [2, 7, 9, 3, 1]

    Best choice:
    2 + 9 + 1 = 12

    Return:
    12

    DP meaning:
    - dp[i] means the maximum money from the first i houses

    Important:
    - nums[i - 1] is the money in the ith house

    Base cases:
    - dp[0] = 0
    - dp[1] = nums[0]

    Transition:
    - dp[i] = max(
        dp[i - 1],
        dp[i - 2] + nums[i - 1]
      )

    Edge cases:
    - if nums is empty, return 0
    """
    # TODO: write your code here
    if not nums:
        return 0
    
    dp = [0] * (len(nums)+1) 

    dp[0] = 0
    dp[1] = nums[0]

    for i in range(2, len(nums)+1):
        skip_current = dp[i - 1]
        rob_current = dp[i - 2] + nums[i-1]
        dp[i] = max(skip_current, rob_current)
        

    return dp[len(nums)]
        
        
        
    
    


def rob_variables(nums):
    """
    Return the maximum amount of money using two variables.

    This is the space-optimized version.
    """
    # TODO: write your code here
    if not nums:
        return 0
    
    prev2 = nums[0] 
    prev1 = 0 

    for i in range(2, len(nums) + 1):
        rob_current = nums[i-1] + prev1
        skip_current = prev2
        current = max(skip_current, rob_current)
        prev1 = prev2
        prev2 = current

    return prev2

def main():
    print(rob([2, 7, 9, 3, 1]))
    print(rob([1, 2, 3, 1]))
    print(rob([5]))
    print(rob([]))

    print("\nVariables:")
    print(rob_variables([2, 7, 9, 3, 1]))
    print(rob_variables([1, 2, 3, 1]))
    print(rob_variables([5]))
    print(rob_variables([]))

    print("\nExpected:")
    print("12")
    print("4")
    print("5")
    print("0")
    print("12")
    print("4")
    print("5")
    print("0")


if __name__ == "__main__":
    main()
