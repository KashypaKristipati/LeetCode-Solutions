from typing import List, Optional

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Approach: Dynamic programming to build up a table of minimum coin changes.
        Time Complexity: O(n*m), where n is the number of denominations and m is the target amount.
        Space Complexity: O(n*m)
        """
        
        # Initialize a list to store the minimum number of coins for each amount from 0 to target
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins are needed to make 0 amount

        # Iterate over each coin denomination
        for coin in coins:
            # Iterate over each amount from the coin value up to the target
            for i in range(coin, amount + 1):
                # Update the minimum number of coins for the current amount if using the current coin results in fewer coins
                dp[i] = min(dp[i], dp[i - coin] + 1)

        # If no combination of coins can make the target amount, return -1
        return dp[amount] if dp[amount] != float('inf') else -1

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.change(10, [1, 2, 5]))  # Expected: 3
    print(s.change(0, [1, 2, 5]))  # Expected: 0
    print(s.change(3, [2]))  # Expected: -1