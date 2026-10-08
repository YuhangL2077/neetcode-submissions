class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, nums[i] + i)

            if farthest >= len(nums) - 1:
                return True

        return True