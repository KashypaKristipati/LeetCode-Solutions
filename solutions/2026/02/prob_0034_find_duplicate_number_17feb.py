def findDuplicate(nums: List[int]) -> int:
    """
    Approach: Floyd's Tortoise and Hare Algorithm
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    This algorithm uses two pointers that move at different speeds through the list.
    The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
    When they meet, it means there is a duplicate in the list.
    """
    # Phase 1: Detecting the cycle using Floyd's Tortoise and Hare Algorithm
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    # Phase 2: Finding the start of the cycle (the duplicate number)
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare