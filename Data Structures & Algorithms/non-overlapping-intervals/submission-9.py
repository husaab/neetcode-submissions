class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # you establish a while loop, like while interval

        result = 0

        intervals.sort(key=lambda interval: interval[0])

        curr_overlap = intervals[0]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < curr_overlap[1]:
                result+=1

                if intervals[i][1] < curr_overlap[1]:
                    curr_overlap = intervals[i]
            else:
                curr_overlap = intervals[i]
        
        return result