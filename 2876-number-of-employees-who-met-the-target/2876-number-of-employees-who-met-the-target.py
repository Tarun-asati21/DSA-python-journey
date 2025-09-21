class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        # # brute force
        # count=0
        # for hr in hours :
        #     if hr >= target :
        #         count+=1
        # return count

        # better solution -> binary search - upper bound
        hours_=sorted(hours)
        mini=len(hours)
        l=0
        r=len(hours)-1
        while l<=r :
            m=(l+r)//2
            if hours_[m] >= target:
                mini=min(mini, m)
                r=m-1
            else :
                l=m+1
        return len(hours_[mini:])
