"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda interval : interval[0])

        for i in range(1, len(intervals)):
            previous_end = intervals[i - 1][1]
            current_start = intervals[i][0]

            if current_start < previous_end:
                return False

        return True