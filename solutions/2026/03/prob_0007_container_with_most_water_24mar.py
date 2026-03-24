from typing import List, Optional

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Approach: Two pointers technique with a two-pointer approach to track the maximum area.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Initialize variables
        left = 0
        right = len(height) - 1
        max_area = 0

        # Loop until the two pointers meet
        while left < right:
            # Calculate the area of the current rectangle
            current_area = min(height[left], height[right]) * (right - left)

            # Update the maximum area if necessary
            max_area = max(max_area, current_area)

            # Move the pointer that corresponds to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area