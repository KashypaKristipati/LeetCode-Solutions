from typing import List, Optional

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Approach: We use a hashmap to store the sorted version of each string as key and its original anagram as value.
        Time Complexity: O(NMlogM) where N is the number of strings and M is the maximum length of a string.
        Space Complexity: O(NM) for storing all the strings in the hashmap.
        """
        # Create a hashmap to store the sorted version of each string as key and its original anagram as value
        anagrams = {}
        for s in strs:
            # Sort the characters in the string and use it as the key in the hashmap
            sorted_s = "".join(sorted(s))
            if sorted_s not in anagrams:
                anagrams[sorted_s] = []
            # Add the original string to the list of its anagram
            anagrams[sorted_s].append(s)
        return list(anagrams.values())

# --- Test Cases ---
if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # Expected: [["eat","tea","ate"],["tan","nat"],["bat"]]
    print(s.groupAnagrams(["a"]))  # Expected: [["a"]]
    print(s.groupAnagrams([]))  # Expected: []