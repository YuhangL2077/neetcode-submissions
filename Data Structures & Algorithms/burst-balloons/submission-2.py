class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + nums + [1]
        n = len(arr)
        memo = {}

        def dfs(left, right):
            # no balloon between left and right
            if left + 1 == right:
                return 0
            if (left, right) in memo:
                return memo[(left, right)]
            # k = last balloon to burst
            max_coins = 0
            for k in range(left + 1, right):
                coins = (
                    dfs(left, k) + arr[left]*arr[k]*arr[right] + dfs(k, right)
                )

                max_coins = max(max_coins, coins)

            memo[(left, right)] = max_coins
            return max_coins

        return dfs(0, n-1)
        