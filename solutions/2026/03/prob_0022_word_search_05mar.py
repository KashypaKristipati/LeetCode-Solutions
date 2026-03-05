from typing import List, Optional

class Solution:
    def wordSearch(self, board: List[List[str]], word: str) -> bool:
        """
        Approach: 
        Time Complexity: O(R*C*N) where R is the number of rows, C is the number of columns, and N is the length of the word.
        Space Complexity: O(R*C)
        """
        # Define the directions for DFS
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Function to check if a cell is within the board
        def is_valid(x, y):
            return 0 <= x < len(board) and 0 <= y < len(board[0])

        # Function to perform DFS
        def dfs(x, y, i):
            # If the current character does not match the character in the word, return False
            if board[x][y] != word[i]:
                return False

            # If we have found all characters in the word, return True
            if i == len(word) - 1:
                return True

            # Mark the current cell as visited
            temp = board[x][y]
            board[x][y] = '#'

            # Perform DFS in all directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny) and dfs(nx, ny, i + 1):
                    return True

            # Unmark the current cell
            board[x][y] = temp

            # If we have not found all characters in the word, return False
            return False

        # Perform DFS from each cell in the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        # If we have not found the word in the board, return False
        return False

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.wordSearch([["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]], "ABCCED"))  # Expected: True
    print(s.wordSearch([["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]], "SEE"))  # Expected: True
    print(s.wordSearch([["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]], "ABCB")))  # Expected: False