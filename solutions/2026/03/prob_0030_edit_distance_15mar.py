def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill the rest of the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1

            dp[i][j] = min(dp[i - 1][j] + 1,      # Deletion
                           dp[i][j - 1] + 1,      # Insertion
                           dp[i - 1][j - 1] + substitution_cost)  # Substitution

    return dp[m][n]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Approach: Dynamic Programming. The idea is to build a table where each cell [i][j] represents the minimum number of operations (insertions, deletions and substitutions) needed to transform the first i characters of word1 into the first j characters of word2.
        
        Time Complexity: O(m*n), where m and n are the lengths of the two words. This is because we need to fill in a table of size (m+1)*(n+1).
        
        Space Complexity: O(m*n), as we need to store the entire table in memory.
        """
        # step-by-step implementation
        return minDistance(word1, word2)