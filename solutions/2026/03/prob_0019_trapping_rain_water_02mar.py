from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Approach: Two Pointers Technique with two arrays to track max heights on the left and right sides.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Initialize two pointers, one at the start and one at the end of the array
        left, right = 0, len(height) - 1
        # Initialize the maximum heights on the left and right sides
        max_left, max_right = 0, 0
        # Initialize the total trapped water
        total_water = 0

        # Loop until the two pointers meet
        while left < right:
            # If the height on the left side is less than the height on the right side
            if height[left] < height[right]:
                # If the height on the left side is greater than the max height on the left side
                if height[left] > max_left:
                    # Update the max height on the left side
                    max_left = height[left]
                else:
                    # Calculate the trapped water and add it to the total
                    total_water += max_left - height[left]
                # Move the left pointer to the right
                left += 1
            else:
                # If the height on the right side is greater than the max height on the right side
                if height[right] > max_right:
                    # Update the max height on the right side
                    max_right = height[right]
                else:
                    # Calculate the trapped water and add it to the total
                    total_water += max_right - height[right]
                # Move the right pointer to the left
                right -= 1

        # Return the total trapped water
        return total_water

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.trap([0,1,0,2,1,0,5,3,4]))  # Expected: 9
    print(s.trap([4,2,0,3,2,5]))  # Expected: 9
    print(s.trap([0,1,0,2,1,0,1,3,2,4]))  # Expected: 10