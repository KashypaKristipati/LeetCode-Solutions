from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Approach: Dynamic programming. We create a 2D array dp where dp[i][j] represents the number of unique paths from (0,0) to (i,j).
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        """
        # Initialize a 2D array dp with zeros
        dp = [[0]*n for _ in range(m)]
        
        # There is only one way to reach each cell in the first row and first column
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        # Fill up the rest of the dp array
        for i in range(1, m):
            for j in range(1, n):
                # The number of unique paths to cell (i,j) is the sum of the number of unique paths to cell (i-1,j) and cell (i,j-1)
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # The number of unique paths to the bottom-right cell is the answer
        return dp[m-1][n-1]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 7))  # Expected: 28
    print(s.uniquePaths(3, 2))  # Expected: 3
    print(s.uniquePaths(7, 3))  # Expected: 28
    print(s.uniquePaths(3, 3))  # Expected: 6