class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lst=[]
        for i in range(0,len(nums)):
            count=0
            for j in range (0, len(nums)):
                if nums[j]<nums[i]:
                    count+=1
            lst.append(count)
        return lst
