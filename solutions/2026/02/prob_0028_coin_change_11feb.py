from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.change(10, [1, 2, 5]))  # Expected: 3
    print(s.change(0, [1, 2, 5]))   # Expected: 0
    print(s.change(3, [2]))          # Expected: -1