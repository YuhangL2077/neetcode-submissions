class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for num in nums:
            if not tails or num > tails[-1]:
                tails.append(num)
            else:
                left = 0
                right = len(tails) - 1

                while left < right:
                    mid = (left + right) // 2

                    if tails[mid] >= num:
                        right = mid
                    else:
                        left = mid + 1

                tails[left] = num

        return len(tails)