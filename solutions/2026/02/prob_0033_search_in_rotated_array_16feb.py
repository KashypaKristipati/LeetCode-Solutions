from typing import List, Optional

class Solution:
    def search(self, nums: List[int], target: int) -> Optional[int]:
        """
        Approach: 
        We use a modified binary search algorithm to find the target in the rotated array.
        If the target is found, we return its index. Otherwise, we return -1.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # Check if the input list is empty
        if not nums:
            return -1

        # Initialize two pointers for binary search
        left, right = 0, len(nums) - 1

        # Continue the search until the two pointers meet
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2

            # If the target is found at the middle index, return it
            if nums[mid] == target:
                return mid

            # If the left half is sorted
            if nums[left] <= nums[mid]:
                # If the target is in the left half, update the right pointer
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # Otherwise, update the left pointer
                else:
                    left = mid + 1
            # If the right half is sorted
            else:
                # If the target is in the right half, update the left pointer
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # Otherwise, update the right pointer
                else:
                    right = mid - 1

        # If the target is not found, return -1
        return -1

# --- Test Cases ---
if __name__ == "__main__":
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], 0))  # Expected: 4
    print(s.search([4,5,6,7,0,1,2], 3))  # Expected: -1