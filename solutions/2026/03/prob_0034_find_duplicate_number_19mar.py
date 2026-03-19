def findDuplicate(nums: List[int]) -> int:
    """
    Approach: Floyd's Tortoise and Hare Algorithm
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    tortoise = nums[0]
    hare = nums[0]

    # Phase 1: Detect cycle using slow and fast pointers
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        
        if tortoise == hare:
            break

    # Phase 2: Find the start of the cycle (the duplicate number)
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare