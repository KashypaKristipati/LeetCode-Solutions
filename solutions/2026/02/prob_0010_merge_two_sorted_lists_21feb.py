from typing import List

class Solution:
    def mergeTwoLists(self, l1: List[int], l2: List[int]) -> List[int]:
        """
        Approach: Merge two sorted lists into one sorted list.
        Time Complexity: O(n + m) where n and m are the lengths of the two lists.
        Space Complexity: O(n + m) where n and m are the lengths of the two lists.
        """
        # Initialize the result list
        result = []
        
        # Initialize two pointers, one for each list
        i, j = 0, 0
        
        # Merge the lists
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                result.append(l1[i])
                i += 1
            else:
                result.append(l2[j])
                j += 1
        
        # Append the remaining elements, if any
        result.extend(l1[i:])
        result.extend(l2[j:])
        
        return result

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.mergeTwoLists([1,2,3], [2,4,5]))  # Expected: [1,2,2,3,4,5]
    print(s.mergeTwoLists([1], [1]))  # Expected: [1,1]
    print(s.mergeTwoLists([1,2,3], []))  # Expected: [1,2,3]
    print(s.mergeTwoLists([], [1,2,3]))  # Expected: [1,2,3]