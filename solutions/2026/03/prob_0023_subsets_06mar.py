from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Backtracking
        Time Complexity: O(2^n)
        Space Complexity: O(2^n)
        """
        def backtrack(start, path):
            # Add the current path to the result
            result.append(path)
            # Iterate over the remaining elements
            for i in range(start, len(nums)):
                # Add the current element to the path
                backtrack(i + 1, path + [nums[i]])
        
        # Initialize the result
        result = []
        # Start the backtracking process
        backtrack(0, [])
        return result

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))  # [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]