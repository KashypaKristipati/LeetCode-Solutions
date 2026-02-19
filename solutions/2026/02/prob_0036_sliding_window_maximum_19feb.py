from typing import List, Optional
import heapq

class Solution:
    def maxSlidingMaximum(self, nums: List[int]) -> List[Optional[int]]:
        """
        Approach: We use a deque to store indices of elements in descending order.
        Time Complexity: O(n log k) where n is the length of nums and k is the size of the deque.
        Space Complexity: O(k)
        """
        # Initialize variables
        n = len(nums)
        max_deque = []  # stores indices of elements in descending order
        min_deque = []  # stores indices of elements in ascending order

        # Preprocess to find the first occurrence of each element
        for i, num in enumerate(nums):
            while max_deque and nums[max_deque[-1]] < num:
                max_deque.pop()
            while min_deque and nums[min_deque[-1]] > num:
                min_deque.pop()
            max_deque.append(i)
            min_deque.append(i)

        # Initialize the result list
        res = [None] * n

        # Process each element in the array
        for i, num in enumerate(nums):
            while max_deque and nums[max_deque[0]] < num:
                max_deque.popleft()
            while min_deque and nums[min_deque[0]] > num:
                min_deque.pop(0)
            if not max_deque:
                res[i] = None
            else:
                res[i] = nums[max_deque[0]]

        return res