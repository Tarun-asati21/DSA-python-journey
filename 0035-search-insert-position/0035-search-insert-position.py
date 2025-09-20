class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # upperbound approach - O(log n)
        mini=len(nums)
        l=0
        r=len(nums)-1
        while l<=r :
            mid=(l+r)//2
            if nums[mid]==target :
                return mid
            elif nums[mid]>target :
                mini = min(mini, mid)
                r=mid-1
            else :
                l=mid+1
        return mini