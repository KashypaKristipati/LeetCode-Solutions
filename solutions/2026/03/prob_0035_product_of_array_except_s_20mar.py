from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Approach: We use two passes over the array to calculate the prefix and suffix products.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        
        # Calculate the length of the input list
        n = len(nums)
        
        # Initialize a list to store the output, with all elements set to 1
        output = [1] * n
        
        # Calculate the prefix products and store them in the output list
        prefix_product = 1
        for i in range(n):
            output[i] *= prefix_product
            prefix_product *= nums[i]
        
        # Calculate the suffix products and multiply with the corresponding prefix product
        suffix_product = 1
        for i in range(n-1, -1, -1):
            output[i] *= suffix_product
            suffix_product *= nums[i]
        
        return output

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))  # Expected: [24, 12, 8, 6]
    print(s.productExceptSelf([1, 1, 1, 1]))  # Expected: [1, 1, 1, 1]
    print(s.productExceptSelf([2, 3, -2, -4]))  # Expected: [-8, 12, -6, 8]