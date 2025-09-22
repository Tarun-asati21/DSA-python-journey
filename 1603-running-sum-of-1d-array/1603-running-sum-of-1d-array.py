class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # running sum = prefix sum
        # aasan bhasa me !!
        
        sumi = 0
        for i in range(0,len(nums)):
            sumi+=nums[i]
            nums[i]=sumi
        return nums