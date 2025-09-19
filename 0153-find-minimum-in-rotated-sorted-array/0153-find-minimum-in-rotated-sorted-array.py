class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums =sorted(nums)
        return nums[0]
        # few edge cases checks :
        # s=len(nums)
        # if s==1 :
        #     return nums[0]
        # if nums[0]>nums[1]:
        #     return nums[1]
        # if nums[-1]<nums[-2]:
        #     return nums[-1]

        # l=0
        # r=s-1
        # while l<r :
        #     m = (l+r)//2
        #     if (nums[m]>nums[m-1] and nums[m]>nums[m+1]) :
        #         return nums[m+1]
        #     elif nums[m]<nums[m-1] and nums[m]<nums[m+1]:
        #         return nums[m]
        #     elif nums[m-1]<nums[m]<nums[m+1]:
        #         r=m-1
        #     else :
        #         l=m+1
        # return -1