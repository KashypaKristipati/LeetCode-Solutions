from typing import List, Optional
import numpy as np

class Solution:
    def rotate(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Approach: Transpose and reverse each row of the input matrix.
        Time Complexity: O(n*m)
        Space Complexity: O(1)
        """
        
        # Get the number of rows and columns in the matrix
        n = len(matrix)
        
        # Transpose the matrix
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse each row of the transposed matrix
        for row in matrix:
            row.reverse()
        
        return matrix

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))  # Expected: [[7,4,1],[8,5,2],[9,6,3]]
    print(s.rotate([[1,2,3],[7,8,9],[4,5,6]]))  # Expected: [[7,4,1],[5,8,2],[9,6,3]]