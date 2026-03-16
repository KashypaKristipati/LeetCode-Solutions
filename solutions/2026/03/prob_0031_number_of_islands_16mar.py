from typing import List, Optional

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Approach: 
            - DFS to traverse each island
            - Mark visited cells by setting them to '0'
        Time Complexity: O(R*C)
        Space Complexity: O(R*C) for the recursion stack
        """
        
        # Check if the grid is empty
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            # Check if the cell is within bounds and is a land cell
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            
            # Mark the cell as visited by setting it to '0'
            grid[r][c] = '0'

            # Recursively visit all adjacent land cells
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        # Iterate over each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell is a land cell and has not been visited yet
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)

        return count

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))  # Expected: 1
    print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))  # Expected: 1
    print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","0","0","0"],["0","0","0","1","1"]]))  # Expected: 2