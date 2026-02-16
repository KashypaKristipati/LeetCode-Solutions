class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Approach: Dynamic Programming
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("leetcode", ["leet", "code"]))  # Expected: True
    print(s.wordBreak("applepenapple", ["apple", "pen"]))  # Expected: True
    print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Expected: False