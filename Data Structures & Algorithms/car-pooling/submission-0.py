class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for num, i, j in trips:
            events.append((i, num))
            events.append((j, -num))

        events.sort(key=lambda x:x[0])
        curr_capacity = 0
        max_capacity = 0
        for event in events:
            curr_capacity += event[1]
            max_capacity = max(max_capacity, curr_capacity)

        return capacity >= max_capacity