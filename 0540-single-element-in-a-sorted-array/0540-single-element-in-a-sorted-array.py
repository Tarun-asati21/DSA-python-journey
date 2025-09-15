class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # # brute force solution -> O(n)
        # s=len(nums)
        # for i in range(s-1,0,-2):
        #     if nums[i]!=nums[i-1]:
        #         return nums[i]
        # return nums[0]
            
        # # optimal solution -> O(logn)
        s=len(nums)
        # handling edge cases 
        if s==1 :
            return nums[0]
        if nums[0]!=nums[1] :
            return nums[0]
        if nums[s-1]!=nums[s-2]:
            return nums[s-1]

        # binary search approach
        low =0
        high = s-1
        while low <= high :
            mid = (high+low)//2
            if nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1] :
                return nums[mid]

            # odd-even index pairing -> right side
            if (mid%2==0 and nums[mid-1]==nums[mid]) or (mid%2==1 and nums[mid]==nums[mid+1]) :
                high=mid-1 # switch to left side

            # even-odd index pairing -> left side 
            else :
                low =mid+1 # switch to right side 
         
        
