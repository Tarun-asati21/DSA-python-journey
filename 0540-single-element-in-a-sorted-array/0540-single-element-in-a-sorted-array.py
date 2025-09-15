class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # brute force solution
        s=len(nums)
        for i in range(s-1,0,-2):
            if nums[i]!=nums[i-1]:
                return nums[i]
        return nums[0]
            

