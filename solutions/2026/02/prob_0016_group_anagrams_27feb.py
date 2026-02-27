from typing import List, Optional
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Approach: Hashing with a twist. We use a hashmap where the key is the sorted version of the string and the value is a list of anagrams.
        Time Complexity: O(NMlogM) where N is the number of strings and M is the maximum length of a string.
        Space Complexity: O(NM) where N is the number of strings and M is the maximum length of a string.
        """
        # Create a hashmap to store the anagrams
        anagrams = defaultdict(list)
        
        # Iterate over each string in the input list
        for s in strs:
            # Sort the characters in the string and use it as the key in the hashmap
            key = "".join(sorted(s))
            # Add the original string to the list of anagrams for the corresponding key
            anagrams[key].append(s)
        
        # Return the list of anagrams
        return list(anagrams.values())

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # Expected: [["eat","tea","ate"],["tan","nat"],["bat"]]
    print(s.groupAnagrams([""]))  # Expected: [[]]
    print(s.groupAnagrams(["a"]))  # Expected: [["a"]]