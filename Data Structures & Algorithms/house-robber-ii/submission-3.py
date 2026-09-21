class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def easyRob(nums):
            if len(nums) == 1:
                return nums[0]
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            # dp[x] stands for maximum amount I can rob in first x houses
            # transition
            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

            return dp[-1]

        exclude_first = easyRob(nums[1:])
        exclude_last = easyRob(nums[:-1])

        return max(exclude_first, exclude_last)

        
        