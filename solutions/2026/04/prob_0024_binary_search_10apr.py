from typing import List, Optional

class Solution:
    def binarySearch(self, nums: List[int], target: int) -> Optional[int]:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return None

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.binarySearch([4,5,6,7,0,1,2], 0))  # Expected: 4
    print(s.binarySearch([4,5,6,7,0,1,2], 3))  # Expected: None
    print(s.binarySearch([1], 0))  # Expected: None
    print(s.binarySearch([], 0))  # Expected: None