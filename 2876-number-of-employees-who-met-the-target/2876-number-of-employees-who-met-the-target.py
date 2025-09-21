class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        # # brute force -> linear search
        # count=0
        # for hr in hours :
        #     if hr >= target :
        #         count+=1
        # return count

        # better solution -> iteration pruning 
        hours=sorted(hours)
        a=len(hours)
        for i in range(0,a):
            if hours[i]>=target :
                a=i
                break
        return len(hours[a:])
