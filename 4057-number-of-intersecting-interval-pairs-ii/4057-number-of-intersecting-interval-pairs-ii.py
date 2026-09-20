import bisect

class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        starts = [interval[0] for interval in intervals]
        
        count = 0
        n= len(intervals)
        for i in range(0, n):
            idx = bisect.bisect_right(starts, intervals[i][1], i+1, n)
            count += idx - (i+1)
        return count