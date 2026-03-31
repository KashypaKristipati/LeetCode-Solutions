from typing import List, Optional
import itertools

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        Approach: This problem can be solved using the concept of permutations and combinations.
        We use the itertools.combinations function to generate all possible substrings of 's' that are of the same length as 't'.
        Then we count the number of these substrings that contain 't'.

        Time Complexity: O(n*m), where n is the length of string s and m is the length of string t.
        Space Complexity: O(1), excluding the space required for the output.

        """
        # Generate all possible substrings of 's' that are of the same length as 't'
        substrings = [''.join(p) for p in itertools.combinations(s, len(t))]
        
        # Count the number of these substrings that contain 't'
        count = sum(1 for substring in substrings if t in substring)
        
        return count

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.numDistinct("rabbbit", "rabbit"))  # Expected: 3
    print(s.numDistinct("hello", "ll"))  # Expected: 2
    print(s.numDistinct("", "a"))  # Expected: 0
    print(s.numDistinct("abc", "d"))  # Expected: 0