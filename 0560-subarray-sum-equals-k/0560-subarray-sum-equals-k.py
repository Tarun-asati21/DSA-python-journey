class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        from collections import defaultdict 
        sum_map=defaultdict(int)
        sum_map={0:1}

        n = len(nums)
        sumi=0
        count=0
        for i in range(0,n):
            sumi+=nums[i]
            rem=sumi-k
            count += sum_map.get(rem, 0)
            sum_map[sumi] = sum_map.get(sumi,0) + 1
        return count