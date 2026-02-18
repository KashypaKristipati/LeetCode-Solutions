from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Approach: We use two passes over the array to calculate the prefix and suffix products.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        
        # Initialize an array to store the output
        output = [0] * len(nums)
        
        # Calculate the prefix product for each element
        prefix_product = 1
        for i in range(len(nums)):
            output[i] = prefix_product
            prefix_product *= nums[i]
        
        # Calculate the suffix product for each element and multiply it with the corresponding prefix product
        suffix_product = 1
        for i in reversed(range(len(nums))):
            output[i] *= suffix_product
            suffix_product *= nums[i]
        
        return output

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))  # Expected: [24,12,8,6]
    print(s.productExceptSelf([1,1,1,1]))  # Expected: [1,1,1,1]