class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #关心的问题是：凑出金额x，最少需要多少枚硬币？
        #所以dp[x] = 凑出金额x所需要的最少硬币数量
        # 如果最后用了 1：
        # dp[7] = dp[6] + 1

        # 如果最后用了 2：
        # dp[7] = dp[5] + 1

        # 如果最后用了 5：
        # dp[7] = dp[2] + 1

        # dp[7] = min(dp[x], dp[x - coin] + 1)

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for curr_amount in range(1, amount + 1):
            for coin in coins:
                if curr_amount >= coin:
                    dp[curr_amount] = min(
                        dp[curr_amount],
                        dp[curr_amount - coin] + 1
                    )

        return dp[amount] if dp[amount] != float("inf") else -1
