class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):    
            curr_weight = 0
            used_days = 1

            for weight in weights:
                if curr_weight + weight > capacity:
                    used_days += 1
                    curr_weight = 0
                
                curr_weight += weight

            return used_days <= days

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            if canShip(mid):
                right = mid
            else:
                left = mid + 1

        return left
                    