class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # brute force -> using sorting 
        nums=sorted(nums, reverse=True)
        return nums[k-1]
