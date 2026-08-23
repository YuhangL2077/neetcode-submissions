class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        window_count = Counter()
        length_s1 = len(s1)
        length_s2 = len(s2)
        l = 0
        for r in range(len(s2)):
            window_count[s2[r]] = window_count.get(s2[r], 0) + 1
            if r - l + 1 > length_s1:
                window_count[s2[l]] = window_count.get(s2[l]) - 1
                l += 1
            if r - l + 1 == length_s1:
                if window_count == count:
                    return True
        return False


        