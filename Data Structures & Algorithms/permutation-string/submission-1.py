class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        length_s1 = len(s1)
        length_s2 = len(s2)
        l = 0
        while l <= length_s2 - length_s1:
            if Counter(s2[l: l + length_s1]) == count:
                return True
            l += 1

        return False

        