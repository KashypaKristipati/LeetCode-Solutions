def mergeTwoLists(l1: Optional[List[int]], l2: Optional[List[int]]) -> Optional[List[int]]:
    """
    Approach: We will use a two-pointer technique to compare the elements of both lists and merge them into one sorted list.
    Time Complexity: O(n + m) where n and m are the lengths of the input lists.
    Space Complexity: O(n + m) for the output list.
    """
    # Initialize the output list
    merged_list = []
    
    # Initialize two pointers, one for each list
    i = j = 0
    
    # Loop until we have processed all elements in both lists
    while i < len(l1) and j < len(l2):
        # If the current element in l1 is smaller, append it to the output list and move the pointer
        if l1[i] < l2[j]:
            merged_list.append(l1[i])
            i += 1
        # If the current element in l2 is smaller, append it to the output list and move the pointer
        else:
            merged_list.append(l2[j])
            j += 1
    
    # If there are remaining elements in l1, append them to the output list
    while i < len(l1):
        merged_list.append(l1[i])
        i += 1
    
    # If there are remaining elements in l2, append them to the output list
    while j < len(l2):
        merged_list.append(l2[j])
        j += 1
    
    # Return the merged list
    return merged_list