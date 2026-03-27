class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: We will create a new list and append elements from both lists to it.
        Time Complexity: O(n + m) where n and m are the lengths of the two input lists
        Space Complexity: O(n + m) for the new list
        """
        # Create a new ListNode with value 0 as the dummy node
        dummy = ListNode(0)
        current = dummy

        # While both lists have elements
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # If one list is longer than the other, append its remaining elements to the new list
        if l1:
            current.next = l1
        elif l2:
            current.next = l2

        # Return the next node of the dummy node (the actual start of the merged list)
        return dummy.next