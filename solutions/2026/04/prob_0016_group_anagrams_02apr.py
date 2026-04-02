from typing import List, Optional
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Approach: Hashing with a sorted string key.
        Time Complexity: O(NMlogM) where N is the number of strings and M is the maximum length of a string.
        Space Complexity: O(NM) for storing all anagrams in the hashmap.
        """
        # Create a hashmap to store anagrams
        anagram_map = collections.defaultdict(list)
        
        # Iterate over each input string
        for word in strs:
            # Sort the characters in the string and use it as key
            sorted_word = "".join(sorted(word))
            
            # Add the original word to the list of values for this key
            anagram_map[sorted_word].append(word)
        
        # Return all values (anagrams) in the hashmap
        return [words for words in anagram_map.values()]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # Expected: [["eat","tea","ate"],["tan","atn"],["bat"]]
    print(s.groupAnagrams(["a"]))  # Expected: [["a"]]
    print(s.groupAnagrams(["aa"]))  # Expected: [["aa"]]