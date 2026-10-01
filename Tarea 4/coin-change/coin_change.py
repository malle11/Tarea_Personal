class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        IMPOSIBLE = amount + 1

        dp = [0] + [IMPOSIBLE] * amount

        for x in range(1, amount + 1):
            for moneda in coins:
                if moneda <= x and dp[x - moneda] + 1 < dp[x]:
                    dp[x] = dp[x - moneda] + 1

        return -1 if dp[amount] == IMPOSIBLE else dp[amount]