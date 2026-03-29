from typing import List, Optional

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Approach: This problem can be solved using dynamic programming.
        We initialize a list dp where dp[i] represents the maximum reachable index from the ith position.
        We iterate through the array and update dp[i] to be the maximum of its current value and 1 plus the last element at index i-1.
        Finally, we return the last element in dp which represents the maximum reachable index.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(nums)
        if n <= 1:
            return 0
        dp = [nums[0]]
        for i in range(1, n):
            # update dp[i] to be the maximum of its current value and 1 plus the last element at index i-1.
            dp.append(max(dp[-1], nums[i]))
        # return the last element in dp which represents the maximum reachable index.
        return max(dp) - 1

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.jump([2,3,1,0,4]))  # Expected: 2
    print(s.jump([2,3,0,1,4]))  # Expected: 2
    print(s.jump([0,1,2,3,4]))  # Expected: 4