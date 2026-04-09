from typing import List, Optional

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Backtracking
        Time Complexity: O(2^n)
        Space Complexity: O(n)
        """
        # Initialize result list with an empty subset
        result = [[]]
        
        # Iterate over each number in the input list
        for num in nums:
            # For each existing subset, create a new subset by appending the current number
            result += [curr + [num] for curr in result]
        
        return result

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))  # Expected: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    print(s.subsets([0]))  # Expected: [[], [0]]