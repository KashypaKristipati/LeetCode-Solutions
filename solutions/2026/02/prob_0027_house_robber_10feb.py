from typing import List, Optional

class Solution:
    def houseRobber(self, nums: List[int]) -> int:
        """
        Approach: This problem can be solved using dynamic programming.
        The idea is to consider two cases for each house: rob it or don't rob it.
        We use a list dp where dp[i] represents the maximum amount of money we can get by considering the first i houses.

        Time Complexity: O(n)
        Space Complexity: O(n)

        :param nums: A list of integers representing the amount of money in each house
        :return: The maximum amount of money that can be robbed from the given houses
        """
        if not nums:
            return 0

        # Initialize dp array with zeros
        n = len(nums)
        dp = [0] * (n + 1)

        # Base case: We can rob the first house, so we set dp[1] to nums[0]
        dp[1] = nums[0]

        # Fill up the dp array using the two cases
        for i in range(2, n + 1):
            # If we don't rob the current house, then dp[i] is equal to dp[i - 1]
            # If we rob the current house, then dp[i] is equal to nums[i - 1] plus dp[i - 2]
            dp[i] = max(dp[i - 1], nums[i - 1] + dp[i - 2])

        # The maximum amount of money that can be robbed from all houses is stored in dp[n]
        return dp[n]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.houseRobber([1,2,3,1]))  # Expected: 4
    print(s.houseRobber([2,7,9,3,1]))  # Expected: 12