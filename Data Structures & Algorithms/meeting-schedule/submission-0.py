"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # i think the way we can identify this easily is by sorting
        # by the second interval, for intervals, and seeing, if end interval of i
        # is greter than interval i +1 start, return true

        intervals.sort(key=lambda interval: interval.start)
    
        start_interval = 0

        while start_interval < len(intervals) - 1:
            start_meeting_end_time = intervals[start_interval].end

            next_meeting_start_time = intervals[start_interval+1].start

            if next_meeting_start_time < start_meeting_end_time:
                return False

            start_interval+=1
        
        return True
