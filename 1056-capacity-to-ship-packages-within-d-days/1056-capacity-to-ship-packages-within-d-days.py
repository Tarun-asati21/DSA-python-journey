class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def count_days(arr,weight):
            count=1
            sumi=0
            for i in arr:
                if sumi + i > weight :
                    count+=1
                    sumi = 0
                sumi += i
            return count
         
        l=max(weights)  # largest packet bhi ship pr aa jaye
        r=sum(weights)  # saare packet ek din me bhi jaa sake  
        while l<=r :
            m=(l+r)//2
            if count_days(weights, m) <= days :
                result=m
                r=m-1
            else :
                l=m+1
        return result
