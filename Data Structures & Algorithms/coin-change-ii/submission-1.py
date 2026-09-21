class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[x] = 凑出x的方案数量
        # dp[x] += dp[x - coin]

        #coin 外层相当于强制规定：组合必须按照 coin 的处理顺序建立。
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(1, amount + 1):
                if i >= coin:
                    dp[i] += dp[i - coin]

        return dp[amount]