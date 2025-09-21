class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        lst=[]
        for i in range(0,len(nums)):
            if i == 0 :
                leftsum=0
            else :
                leftsum=sum(nums[:i])
                
            if i == len(nums)-1 :
                rightsum=0
            else :
                rightsum=sum(nums[i+1:])
            diff=abs(leftsum-rightsum)
            lst.append(diff)
        return lst
