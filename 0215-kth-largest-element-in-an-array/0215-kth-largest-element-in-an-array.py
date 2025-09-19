class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # -> using sorting 
        # nums=sorted(nums, reverse=True)
        # return nums[k-1]

        # -> using maxheap
        # from heapq import heapify, heappush , heappop

        # nums=[-num for num in nums]
        # heapify(nums)
        # for i in range(k):
        #     result = heappop(nums)
        # return -result

        # optimal space solution -> using min heap
        import heapq

        heapify(nums)
        while len(nums)>k:
            heappop(nums)
        return nums[0]