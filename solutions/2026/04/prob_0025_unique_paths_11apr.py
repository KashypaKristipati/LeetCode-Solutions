from typing import List, Optional

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Approach: This problem can be solved using dynamic programming.
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        """
        # Create a 2D array to store the number of unique paths for each cell
        dp = [[0]*n for _ in range(m)]

        # Initialize the first row and column with 1, since there is only one way to reach any cell in the first row or column (from the top-left corner)
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # Fill in the rest of the array using dynamic programming
        for i in range(1, m):
            for j in range(1, n):
                # The number of unique paths to cell (i,j) is the sum of the number of unique paths to the cell above it and the cell to its left
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # The total number of unique paths is stored in the bottom-right corner of the array
        return dp[m-1][n-1]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 7))  # Expected: 28
    print(s.uniquePaths(3, 2))  # Expected: 3
    print(s.uniquePaths(7, 3))  # Expected: 28