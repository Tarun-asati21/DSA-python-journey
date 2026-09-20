class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        # brute force 
        count = 0
        for i in range(0, len(intervals)):
            min1= intervals[i][0]
            max1 =intervals[i][1]
            for j in range(i+1, len(intervals)):
                min2 = intervals[j][0]
                max2 = intervals[j][1]
                if min1 <= min2 <= max1 or min2 <= min1 <= max2 :
                    count+=1
        return count

