class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # brute force solution -> linear search -> O(n)
        if len(nums)==1:
            return 0
        elif len(nums)==2:
            if nums[0]>nums[1]:
                return 0
            else :
                return 1
        else :
            for i in range(0, len(nums)-1):
                if nums[i] > nums[i-1] and nums[i]>nums[i+1] :
                    return i
        return len(nums)-1