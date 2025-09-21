class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        temp = sum(nums)
        count=0
        while temp%k != 0 :
            temp-=1
            count+=1
        return count