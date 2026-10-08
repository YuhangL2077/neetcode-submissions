class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        curr_end = 0
        jumps = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, nums[i] + i)

            if i == curr_end:
                jumps += 1
                curr_end = farthest

        return jumps