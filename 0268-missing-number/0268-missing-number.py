class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        lst=[]
        n=len(nums)
        for i in range (0,n+1) :
            lst.append(i)
        
        missing_num = list(set(lst)-set(nums))
        return missing_num[0]