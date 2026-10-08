class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # if end > start of next, then thats overlapping and need to merge them
        # and we mainly should only do such a thing where we check if
        # end of curr is less than end of next, if it is, then merge

        intervals.sort(key=lambda interval: (interval[0], -interval[1]))
        result = [intervals[0]]

        result_interval = 0

        for i in range(1, len(intervals)):
            curr_interval = intervals[i]
            curr_interval_start = curr_interval[0]
            curr_interval_end = curr_interval[1]

            if curr_interval_start <= result[result_interval][1]:
                if result[result_interval][1] < curr_interval_end:
                    result[result_interval][1] = curr_interval_end
            else:
                result.append(curr_interval)
                result_interval+=1
        
        return result
        


        