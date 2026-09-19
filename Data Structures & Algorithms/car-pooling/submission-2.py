class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for num, i, j in trips:
            events.append((i, num))
            events.append((j, -num))

        # events.sort(key=lambda x:x[0])
        events.sort() # must get off car first, and get on car after
        curr_capacity = 0
        for event in events:
            curr_capacity += event[1]
            if curr_capacity > capacity:
                return False

        return True