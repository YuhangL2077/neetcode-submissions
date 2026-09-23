class Solution:
    def numDecodings(self, s: str) -> int:
    #dp[i] stands for number of decode ways of s[:i]
    #dp[j] = dp[i] + dp[i:j] if dp[i]
        dp = [0] * (len(s) + 1)
        dp[0] = 1

        for i in range(1, len(s) + 1):
            # use one digit
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]

            # use two digits
            if i >= 2 and 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]