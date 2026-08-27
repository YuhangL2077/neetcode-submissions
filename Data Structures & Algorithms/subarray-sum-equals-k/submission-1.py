class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num

            need = curr_sum - k

            if need in prefix_count:
                count += prefix_count[need]

            prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1
            # print(prefix_count)

        return count

# prefix[r] - prefix[l - 1] = k
# prefix[l - 1] = prefix[r] - k
