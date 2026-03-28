def maxSubArray(nums: List[int]) -> int:
    """
    Approach: Kadane's Algorithm
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
    
    current_sum = max_sum = nums[0]
    
    for num in nums[1:]:
        # Update current sum to be the maximum of the current number and the sum of the current number and previous current sum
        current_sum = max(num, current_sum + num)
        
        # Update max sum if current sum is greater than max sum
        max_sum = max(max_sum, current_sum)
    
    return max_sum