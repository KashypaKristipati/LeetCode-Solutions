from typing import List, Optional

class Solution:
    def search(self, nums: List[int], target: int) -> Optional[int]:
        """
        Approach: Binary search algorithm is used to find the target element in the sorted array.
        Time Complexity: O(log n) where n is the number of elements in the array.
        Space Complexity: O(1) as it only uses a constant amount of space.
        """
        # Initialize two pointers, one at the start and one at the end of the array
        left, right = 0, len(nums) - 1
        
        # Continue the search until the two pointers meet
        while left <= right:
            # Calculate the middle index
            mid = left + (right - left) // 2
            
            # If the target is found at the middle index, return it
            if nums[mid] == target:
                return mid
            
            # If the target is less than the middle element, move the right pointer
            elif nums[mid] > target:
                right = mid - 1
            
            # If the target is greater than the middle element, move the left pointer
            else:
                left = mid + 1
        
        # If the target is not found, return None
        return None

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], 0))  # Expected: 4
    print(s.search([4,5,6,7,0,1,2], 3))  # Expected: 4
    print(s.search([4,5,6,7,0,1,2], 8))  # Expected: None