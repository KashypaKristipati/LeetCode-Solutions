from typing import List, Optional

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach: This problem can be solved using backtracking and recursion.
                  We will generate all possible combinations of the given candidates
                  that sum up to the target value. If a valid combination is found,
                  it will be added to the result list.
        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # Sort the candidates array in ascending order
        candidates.sort()
        
        # Initialize an empty list to store the result
        result = []
        
        # Define a helper function for backtracking
        def backtrack(remain, comb, start):
            if remain == 0:
                # If the remaining value is 0, it means we have found a valid combination
                result.append(list(comb))
                return
            elif remain < 0:
                # If the remaining value is less than 0, it means the current combination exceeds the target
                return
            for i in range(start, len(candidates)):
                # Add the current candidate to the current combination
                comb.append(candidates[i])
                # Recursively call the backtrack function with the updated remaining value and combination
                backtrack(remain - candidates[i], comb, i)
                # Remove the last added candidate from the current combination for backtracking
                comb.pop()
        
        # Call the backtrack function with the initial values
        backtrack(target, [], 0)
        
        # Return the result list
        return result

# --- Test Cases ---
if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2,3,5], 8))  # [[2,2,2,2],[3,5]]
    print(s.combinationSum([2,3,6,7], 7))  # [[2,2,3],[7]]