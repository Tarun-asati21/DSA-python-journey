class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def req_time(arr, speed):
            n=len(arr)
            time=0
            for num in arr:
                time=time+ ((num+speed-1)//speed)
            return time
        
        # apply binary search
        l=1
        r=max(piles)
        while l<r :
            mid = (l+r)//2
            time_used = req_time(piles,mid)
            if time_used <= h:
                r=mid
            else: # time_used > h 
                l=mid+1
        return l



                