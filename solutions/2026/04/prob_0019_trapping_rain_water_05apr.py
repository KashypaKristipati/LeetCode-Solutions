from typing import List, Optional

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Approach: 
            We will use two pointers to traverse from both ends of the array towards the center.
            At each step, we calculate the trapped water and move one pointer forward.
            
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        # Initialize variables
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]
        total_water = 0

        # Traverse from both ends towards the center
        while left < right:
            if max_left < max_right:
                left += 1
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    total_water += max_left - height[left]
            elif max_left >= max_right:
                right -= 1
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    total_water += max_right - height[right]

        return total_water

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.trap([0,1,0,2,1,0,5,3,4]))  # Expected: 9
    print(s.trap([4,2,0,3,2,5]))  # Expected: 9
    print(s.trap([1,8,6,2,5,4,8,3,7]))  # Expected: 23