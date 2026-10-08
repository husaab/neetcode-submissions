class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [None] * (amount + 1)

        def checkCoins(remaining_amount):
            if remaining_amount == 0:
                return 0

            if remaining_amount < 0:
                return float("inf")

            if dp[remaining_amount] is not None:
                return dp[remaining_amount]

            least_coins = float("inf")

            for coin in coins:
                # 1. Use this coin and solve the remaining amount.
                # 2. Update least_coins with the minimum.
                least_coins = min(least_coins, 1+ checkCoins(remaining_amount - coin))

            dp[remaining_amount] = least_coins
            return least_coins

        result = checkCoins(amount)

        return -1 if result == float("inf") else result