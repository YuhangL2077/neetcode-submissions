class Solution:
    #prefix[j]%k=prefix[i]%k
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        curr_sum = 0
        remainder_index = {0: -1}

        for i, num in enumerate(nums):
            curr_sum += num
            remainder = curr_sum % k

            if remainder in remainder_index:
                if i - remainder_index[remainder] >= 2:
                    return True
            else:
                remainder_index[remainder] = i

        return False