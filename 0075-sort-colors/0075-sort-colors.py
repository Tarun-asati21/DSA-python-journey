class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n=len(nums)
        for i in range(n-1,0,-1):
            swap = False
            for j in range(0,i) :
                if nums[j] > nums[j+1] :
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    swap = True
            if not swap :
                break
                