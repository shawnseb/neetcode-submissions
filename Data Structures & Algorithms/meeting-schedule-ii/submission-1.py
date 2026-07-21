"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        taken = dict()
        max = 0
        for i in intervals:
            for i in range(i.start, i.end, 1):
                if i in taken:
                    taken[i] = taken[i] + 1
                    if taken[i] > max:
                        max = taken[i]
                else:
                    taken[i] = 1
                    if not taken[i] < max:
                        max = taken[i]
        print(taken)             
        return max

        
        