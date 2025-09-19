class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # brute force -> using sorting 
        # nums=sorted(nums, reverse=True)
        # return nums[k-1]

        # better solution -> using maxheap
        from heapq import heapify, heappush , heappop

        nums=[-num for num in nums]
        heapify(nums)
        for i in range(k):
            result = heappop(nums)
        return -result
