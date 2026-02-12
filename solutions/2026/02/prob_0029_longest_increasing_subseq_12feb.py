from typing import List, Optional

class Solution:
    def longestIncreasingSubsequence(self, nums: List[int]) -> int:
        """
        Approach: Dynamic Programming
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        
        # Handle edge cases
        if not nums:
            return 0
        
        # Initialize dp array with the first element of nums as the only increasing subsequence
        dp = [nums[0]]
        
        # Iterate over each number in nums starting from the second number
        for num in nums[1:]:
            
            # If the current number is greater than the last number in dp, append it to dp
            if not dp or num > dp[-1]:
                dp.append(num)
                
            # Otherwise, find the index of the smallest number in dp that is less than or equal to the current number
            else:
                i = 0
                while i < len(dp) and dp[i] <= num:
                    i += 1
                
                # Replace the smallest number in dp with the current number
                dp[i] = num
        
        # The length of the longest increasing subsequence is the length of dp
        return len(dp)

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.longestIncreasingSubsequence([10,9,2,5,3,7,101,18]))  # Expected: 4
    print(s.longestIncreasingSubsequence([0,1,0,3,2,3]))  # Expected: 4
    print(s.longestIncreasingSubsequence([]))  # Expected: 0