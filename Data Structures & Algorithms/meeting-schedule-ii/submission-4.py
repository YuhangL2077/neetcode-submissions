"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))
        curr = 0
        ans = 0
        #events: [(0,1),(5,1),(10,-1),(15,1),(20,-1),(40,-1)]
        events.sort(key=lambda x:(x[0], x[1]))
        for event in events:
            curr += event[1]
            ans = max(curr, ans)
        return ans

        