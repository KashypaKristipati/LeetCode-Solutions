from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Approach: Transpose and reverse each row of the matrix.
        Time Complexity: O(n*m)
        Space Complexity: O(1)
        """
        n = len(matrix)
        for i in range(n):
            matrix[i] = matrix[i][::-1]
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))  # Expected: [[7,4,1],[8,5,2],[9,6,3]]
    print(s.rotate([[1,2],[3,4]]))  # Expected: [[3,1],[4,2]]
    print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))  # Expected: [[7,4,1],[8,5,2],[9,6,3]]