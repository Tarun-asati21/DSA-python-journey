class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Binary Search -> takes smallest from the sorted part -> and ignore the sorted part
        mini= float("inf") # -> initialises a minimum element equal to infinity
        l=0
        r=len(nums)-1
        while l<=r :
            m = (l+r)//2
            if nums[l]<=nums[m]:
                mini = min(mini, nums[l])
                l=m+1
            else : # nums[m]<nums[r]
                mini=min(mini, nums[m])
                r=m-1      
        return mini