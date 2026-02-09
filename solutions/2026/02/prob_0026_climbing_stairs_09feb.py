def climbStairs(self, steps: int) -> int:
    """
    Approach: This problem can be solved using dynamic programming.
    We initialize a list dp where dp[i] represents the minimum number of steps to reach i-th step.
    The base case is when we are at the first step, so dp[0] = 1. For each subsequent step, 
    we have two options: either take one step or two steps. So, dp[i] = min(dp[i-1], dp[i-2]) + 1.

    Time Complexity: O(n)
    Space Complexity: O(1), as we only use a constant amount of space to store the dp array.
    """
    if steps == 1:
        return 1
    elif steps == 2:
        return 2
    
    # Initialize the first two elements of the dp array
    dp = [0, 1, 2]
    
    # For each step from 3 to n
    for i in range(3, steps + 1):
        # The minimum number of steps to reach this step is the minimum of the previous two steps plus one
        dp.append(min(dp[i-1], dp[i-2]) + 1)
    
    # Return the last element of the dp array, which represents the minimum number of steps to reach the nth step
    return dp[-1]