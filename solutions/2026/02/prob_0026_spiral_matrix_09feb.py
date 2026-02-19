from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, k: int) -> List[List[int]]:
        """
        Approach: We will use a loop to traverse the matrix in a spiral order.
        Time Complexity: O(rows * cols)
        Space Complexity: O(1)
        """
        result = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        direction = 0
        row = col = 0
        for i in range(rows * cols):
            result.append([row + j * k for j in range(k)])
            next_row = row + directions[direction][0]
            next_col = col + directions[direction][1]
            if 0 <= next_row < rows and 0 <= next_col < cols:
                row, col = next_row, next_col
            else:
                direction = (direction + 1) % 4
                row += directions[direction][0]
                col += directions[direction][1]
        return result

# --- Test Cases ---
if __name__ == "__main__":
    s = Solution()
    print(s.spiralMatrixIII(3, 3, 1))  # [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    print(s.spiralMatrixIII(3, 3, 2))  # [[1, 2, 3], [8, 9, 4], [7, 6, 5]]