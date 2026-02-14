from typing import List, Optional

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Approach: 
            - Iterate over each cell in the grid.
            - If a cell is land (represented by 'L'), perform DFS from that cell to mark all adjacent cells as visited ('X').
            - Increment the island count after visiting all cells for an island.

        Time Complexity: O(R*C), where R is the number of rows and C is the number of columns in the grid.
        Space Complexity: O(R*C), due to the recursive call stack in DFS.
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(r, c):
            # Check if cell is within bounds and is land
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 'L':
                return
            # Mark cell as visited
            grid[r][c] = 'X'
            # Perform DFS on adjacent cells
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L':
                    island_count += 1
                    dfs(r, c)

        return island_count

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.numIslands([["L","L","L","L","L"],
                        ["L","L","L","L","L"],
                        ["L","L","L","L","L"],
                        ["L","L","L","L","L"]]))  # Expected: 1
    print(s.numIslands([["L","X","L","X"],
                        ["X","L","X","L"],
                        ["X","L","L","X"],
                        ["X","X","L","X"]]))  # Expected: 1