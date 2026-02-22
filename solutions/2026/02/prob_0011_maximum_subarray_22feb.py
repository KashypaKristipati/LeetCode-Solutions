def maxSubArray(nums: List[int]) -> int:
    """
    Approach: Kadane's Algorithm
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Initialize variables to store the maximum sum and the current sum
    max_sum = float('-inf')
    current_sum = 0

    # Iterate through the array
    for num in nums:
        # Update the current sum to be the maximum of the current number and the sum of the current number and the previous current sum
        current_sum = max(num, current_sum + num)
        
        # Update the maximum sum if the current sum is greater
        max_sum = max(max_sum, current_sum)

    # Return the maximum sum
    return max_sum