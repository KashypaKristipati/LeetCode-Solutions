from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Approach: This problem can be solved using dynamic programming. The idea is to maintain two variables, max_reach and step. max_reach represents the maximum reachable position from the current position, and step represents the number of steps we can take from the current position.
        
        Time Complexity: O(n), where n is the number of elements in the array. This is because we are iterating over the array once.
        
        Space Complexity: O(1), which means the space required does not change with the size of the input array. This is because we are using a constant amount of space to store the variables max_reach and step.
        """
        if not nums:
            return 0

        max_reach = nums[0]
        step = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            if i == max_reach:
                step -= 1
                if step == 0:
                    res += 1
                    step = max_reach
                    max_reach = i + nums[i]
                else:
                    max_reach = i + nums[i]
            else:
                step -= 1

        return res

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.jump([2,3,1,1,4]))  # Expected: 2
    print(s.jump([2,3,0,1,4]))  # Expected: 2
    print(s.jump([1,1,1,1,1]))  # Expected: 4
    print(s.jump([0,1,2,3,4]))  # Expected: 4
    print(s.jump([]))  # Expected: 0