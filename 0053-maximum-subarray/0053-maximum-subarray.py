class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        n=len(nums)
        max_sum=max(nums)
        current_sum = 0
        # if n==1 :
        #     return nums[0]
        # if n==0 :
        #     return 0
        for i in range(0, n):
            current_sum = current_sum + nums[i]
            if current_sum > 0 :
                max_sum=max(current_sum,max_sum)

            else :
                current_sum = 0

        return max_sum

