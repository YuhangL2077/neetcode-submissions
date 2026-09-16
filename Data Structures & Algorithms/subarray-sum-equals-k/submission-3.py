#prefix = [0, 2, 1, 2, 4]  k = 2
#2, 2, 4-2, 4-2 so total is 4
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        prefix_count = {0:1}
        ans = 0
        for num in nums:
            curr_sum += num
            if curr_sum - k in prefix_count:
                ans += prefix_count[curr_sum - k]
            prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1

        return ans




        