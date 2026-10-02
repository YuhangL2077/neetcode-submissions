class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def dfs(i):
            if i == len(nums):
                res.append(path.copy())
                return

            # choice1: choose current num
            path.append(nums[i])
            dfs(i + 1)


            # backtrack
            path.pop()

            # choice2: don't choose current num
            dfs(i + 1)

        dfs(0)
        return res
