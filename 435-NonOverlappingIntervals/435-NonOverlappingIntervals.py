# Last updated: 11/12/2025, 4:57:41 AM
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])

        res = 0

        prev_end = intervals[0][1]
        for start,end in intervals[1:]:

            if prev_end > start:
                prev_end = min(prev_end,end)
                res +=1
            else:
                prev_end = end
        return res