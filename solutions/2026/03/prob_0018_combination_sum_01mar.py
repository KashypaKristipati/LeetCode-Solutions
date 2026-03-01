from typing import List, Optional

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach: Backtracking with sorting and pruning.
        Time Complexity: O(n*m*log(m)) where n is the number of candidates and m is the target.
        Space Complexity: O(n*m) for the recursion stack and the result list.
        """
        # Sort the candidates list in ascending order
        candidates.sort()
        
        # Initialize the result list
        result = []
        
        # Define a helper function for backtracking
        def backtrack(remain, comb, start):
            # If the remaining value is 0, it means we have found a valid combination
            if remain == 0:
                result.append(list(comb))
                return
            
            # Iterate over the candidates starting from the start index
            for i in range(start, len(candidates)):
                # If the current candidate is greater than the remaining value, break the loop
                if candidates[i] > remain:
                    break
                
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
if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))  # Expected: [[2,2,3],[7]]
    print(s.combinationSum([2,3,5], 8))  # Expected: [[2,2,2,2],[2,3,3],[3,5]]
    print(s.combinationSum([2], 1))  # Expected: []