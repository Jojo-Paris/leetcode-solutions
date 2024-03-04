        
        dp = [amount + 1] * (amount + 1)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp[0] = 0
        dp[1] = 1

        for a in range(1, amount + 1):
            for coin in coins:
                a - c >= 0: dp[a] = min(dp[a], 1 + dp[a - c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1
[
