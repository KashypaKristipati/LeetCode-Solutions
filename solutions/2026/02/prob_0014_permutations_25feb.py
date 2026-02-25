from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Recursive backtracking
        Time Complexity: O(n*n!)
        Space Complexity: O(n*n!)
        """
        def backtrack(start, end):
            if start == end:
                result.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1, end)
                nums[start], nums[i] = nums[i], nums[start]
        
        result = []
        backtrack(0, len(nums))
        return result

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))  # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(s.permute([1,1,2]))  # [[1,1,2],[1,2,1]]