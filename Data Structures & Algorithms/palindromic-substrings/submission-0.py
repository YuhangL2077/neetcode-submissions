class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        def expand(left, right):
            nonlocal ans
            while left >= 0 and right < len(s) and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            # odd length: aba
            expand(i, i)
            # even length: abba
            expand(i, i + 1)

        return ans
