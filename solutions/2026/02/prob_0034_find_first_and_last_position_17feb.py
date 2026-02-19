from typing import List, Optional

class Solution:
    def findFirstLastPosition(self, nums: List[int], target: int) -> Optional[List[int]]:
        """
        Approach: 
        We use a combination of binary search and two pointers to solve this problem.
        Time Complexity: O(n + log(m)), where n is the length of nums and m is the number of unique elements in nums.
        Space Complexity: O(1), as we only use a constant amount of space.
        """
        # Find first position
        first = self.findFirst(nums, target)
        
        # If target not found, return [-1, -1]
        if first == -1:
            return [-1, -1]
        
        # Find last position
        last = self.findLast(nums, target)
        
        # Return [first, last]
        return [first, last]

    def findFirst(self, nums: List[int], target: int) -> int:
        """
        Find first occurrence of target in sorted array.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # Check if target found at mid
        if left < len(nums) and nums[left] == target:
            return left
        # Target not found
        return -1

    def findLast(self, nums: List[int], target: int) -> int:
        """
        Find last occurrence of target in sorted array.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        # Check if target found at mid
        if right >= 0 and nums[right] == target:
            return right
        # Target not found
        return -1

# --- Test Cases ---
if __name__ == "__main__":
    s = Solution()
    print(s.findFirstLastPosition([5,7,7,8,8,10], 8))  # Expected: [3,4]
    print(s.findFirstLastPosition([5,7,7,8,8,10], 6))  # Expected: [-1,-1]