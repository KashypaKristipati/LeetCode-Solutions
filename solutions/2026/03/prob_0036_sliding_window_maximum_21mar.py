from typing import List
import heapq

class Solution:
    def maxSlidingMedian(self, nums: List[int], k: int) -> float:
        """
        Approach: We use two heaps to solve this problem. The first heap stores the smaller half of the elements in descending order,
                  and the second heap stores the larger half of the elements in ascending order.
        
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        # Initialize the heaps
        smaller_half = []
        larger_half = []
        
        # Calculate the size of the two halves
        mid = k // 2
        
        for i, num in enumerate(nums):
            # Add elements to the correct heap
            if not larger_half or num > larger_half[0]:
                heapq.heappush(larger_half, -num)
            else:
                heapq.heappush(smaller_half, num)
            
            # Balance the heaps
            if len(smaller_half) > mid + 1:
                heapq.heappush(larger_half, -heapq.heappop(smaller_half))
            elif len(larger_half) > mid:
                heapq.heappush(smaller_half, -heapq.heappop(larger_half))
            
            # Calculate the median
            if k % 2 == 0 and i >= mid:
                median = (-larger_half[0] + smaller_half[0]) / 2
            elif i >= mid:
                median = float(-larger_half[0])
        
        return median

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingMedian([1,2,-3,4], 1))  # Expected: -3
    print(s.maxSlidingMedian([1,2,-3,4], 2))  # Expected: 1