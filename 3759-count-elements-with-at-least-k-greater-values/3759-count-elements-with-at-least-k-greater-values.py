from bisect import bisect_right

class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        if k == 0:
            return len(nums)
        
        nums.sort()
        n = len(nums)
        count = 0
        
        for i in range(n):
            # first index where element > nums[i]
            idx = bisect_right(nums, nums[i])
            
            greater = n - idx
            
            if greater >= k:
                count += 1
        
        return count