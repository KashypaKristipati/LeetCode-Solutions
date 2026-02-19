from typing import List, Optional

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Approach: Kadane's algorithm is used to find the maximum subarray.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Initialize variables for maximum sum and current sum
        max_sum = float('-inf')
        current_sum = 0

        # Iterate over each number in the array
        for num in nums:
            # Update current sum to be the maximum of the current number and the sum of the current number and previous current sum
            current_sum = max(num, current_sum + num)
            
            # Update max sum if current sum is greater than max sum
            max_sum = max(max_sum, current_sum)

        # Return the maximum subarray sum
        return max_sum

# --- Test Cases ---
if __name__ == "__main__":
    s = Solution()
    # Test 1
    print(s.maxSubArray([2, -3, 4, -1]))  # Expected: 6
    # Test 2
    print(s.maxSubArray([-2, -3, 4, -1, -2, 1, 5, -3]))  # Expected: 7