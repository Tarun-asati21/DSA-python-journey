class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Brute force - O(log n^2)
        # first occurence 
        mini=len(nums)
        l=0
        r=len(nums)-1
        while l<=r :
            mid=(l+r)//2
            if nums[mid] == target :
                mini=min(mini, mid)
                r=mid-1
            elif nums[mid] > target :
                r=mid-1
            else :
                l=mid+1

        # last occurence
        maxi=-1
        if mini!=len(nums):
            
            l=0
            r=len(nums)-1
            while l<=r :
                mid =(l+r)//2
                if nums[mid]==target :
                    maxi=max(maxi, mid)
                    l=mid+1
                elif nums[mid] > target :
                    r= mid-1
                else :
                    l=mid+1

        if maxi!= -1 :
            return [mini, maxi]
        else:
            return [-1,-1]