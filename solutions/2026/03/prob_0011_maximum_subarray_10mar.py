def maxSubArray(nums: List[int]) -> int:
    """
    Approach: Kadane's Algorithm
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0

    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum