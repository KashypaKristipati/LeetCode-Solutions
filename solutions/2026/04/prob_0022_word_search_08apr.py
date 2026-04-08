from typing import List, Optional

class Solution:
    def wordSearch(self, board: List[List[str]], word: str) -> bool:
        """
        Approach: 
            We will use a depth-first search (DFS) approach to traverse the board.
            For each cell in the board, we will check if it contains the current character of the word.
            If it does, we will recursively call the DFS function on the adjacent cells.

        Time Complexity: O(N*M), where N is the number of rows and M is the number of columns in the board.
        Space Complexity: O(1), as we only use a constant amount of space to store the current position and direction.
        """
        # Define the directions for DFS
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i: int, j: int, k: int) -> bool:
            """
            Recursive helper function to perform DFS.
            """
            # If the current character does not match the word's character, return False
            if board[i][j] != word[k]:
                return False

            # If we have found all characters of the word, return True
            if k == len(word) - 1:
                return True

            # Mark the current cell as visited by changing its value to a special character
            temp = board[i][j]
            board[i][j] = '#'

            # Perform DFS on the adjacent cells
            for direction in directions:
                ni, nj = i + direction[0], j + direction[1]
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and dfs(ni, nj, k + 1):
                    return True

            # If no path is found, reset the current cell to its original value
            board[i][j] = temp

            # Return False if no path is found
            return False

        # Perform DFS on each cell in the first row
        for j in range(len(board[0])):
            if dfs(0, j, 0):
                return True

        # Perform DFS on each cell in the last column
        for i in range(len(board)):
            if dfs(i, len(board[0]) - 1, 0):
                return True

        # If no path is found, return False
        return False