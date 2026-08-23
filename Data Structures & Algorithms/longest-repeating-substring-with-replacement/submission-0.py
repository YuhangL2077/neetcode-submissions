class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        ans = 0

        for r in range(len(s)):
            # 把 s[r] 加进 window
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(count.values())

            while r - l + 1 - max_freq > k:
                # 从左边 shrink
                count[s[l]] = count.get(s[l]) - 1
                l += 1
                max_freq = max(count.values())
                
            # update answer
            ans = max(ans, r - l + 1)
            
        return ans
        
        