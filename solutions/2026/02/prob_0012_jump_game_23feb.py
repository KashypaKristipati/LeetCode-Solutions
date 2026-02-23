from typing import List, Optional

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Approach: 
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(nums)
        if n <= 1:
            return 0
        max_reach = nums[0]
        step = nums[0]
        res = nums[0]
        for i in range(1, n):
            if i == n - 1:
                return res
            max_reach = max(max_reach, i + nums[i])
            step -= 1
            if step == 0:
                res += 1
                step = max_reach - i
        return res

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.jump([2,3,1,1,4]))  # Expected: 2
    print(s.jump([2,3,0,1,4]))  # Expected: 2
    print(s.jump([1,1,1,1,1]))  # Expected: 4
    print(s.jump([0,1,2,3,4]))  # Expected: 4