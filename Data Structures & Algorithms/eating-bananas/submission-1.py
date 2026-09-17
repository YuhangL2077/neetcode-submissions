class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = max(piles)
        while l < r:
            speed = (l + r) // 2
            time = 0
            for pile in piles:
                if pile <= speed:
                    time += 1
                else:
                    time += math.ceil(pile / speed)
        
            # speed too slow
            if time > h:
                l = speed + 1
            # speed works, but maybe can go faster
            else:
                r = speed
        return l
            

            
        