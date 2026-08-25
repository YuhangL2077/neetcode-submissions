class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        ans = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
        # {
        #     1:1,2:2:3:4
        # } 

        for num, frequency in count.items():
            freq[frequency].append(num)
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
            

        