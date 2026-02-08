from typing import List, Optional

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Approach: Dynamic Programming
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        
        This problem can be solved using dynamic programming. We will create a 2D array dp where dp[i][j] represents the number of unique paths from (0,0) to (i,j).
        
        For each cell in the dp array, we have two options - move right or move down. So, the number of unique paths to reach a cell is the sum of the number of unique paths to reach the cells above and to the left.
        """
        # Create a 2D array to store the number of unique paths
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # Initialize the first row and column, since there is only one way to reach any cell in these rows/columns (by always moving right or down respectively)
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        # Fill the rest of the dp array
        for i in range(1, m):
            for j in range(1, n):
                # The number of unique paths to reach a cell is the sum of the number of unique paths to reach the cells above and to the left
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # The number of unique paths to reach the bottom right cell is the answer
        return dp[m-1][n-1]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 7))  # Expected: 28
    print(s.uniquePaths(10, 20))  # Expected: 500