class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robLine(houses):
            prev2 = 0
            prev1 = 0

            for num in houses:
                curr = max(
                    prev1,        # 不抢当前
                    prev2 + num   # 抢当前
                )

                prev2 = prev1
                prev1 = curr

            return prev1

        return max(
            robLine(nums[:-1]),
            robLine(nums[1:])
        )