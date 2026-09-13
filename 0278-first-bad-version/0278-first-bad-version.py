# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # brute force solution : 
        # for i in range(1,n+1) :
        #     if isBadVersion(i) == True :
        #         return i

        # binary solution
        l,r = 0, n
        while l<=r :
            mid = l + (r-l)//2
            if isBadVersion(mid) == True :
                r = mid - 1
                last_bad = mid
            else :
                l = mid + 1
        
        return last_bad
