"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        timeline = []
        ans = 0
        room = 0
        for interval in intervals:
            timeline.append((interval.start,1))
            timeline.append((interval.end,-1))
        timeline.sort(key=lambda x:(x[0], x[1]))
        for time in timeline:
            room += time[1]
            ans = max(ans, room)

        return ans



            
        