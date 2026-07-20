"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        time = set()
        for i in intervals:
            for j in range(i.start, i.end, 1):
                if j in time:
                    return False
                time.add(j)
        return True
