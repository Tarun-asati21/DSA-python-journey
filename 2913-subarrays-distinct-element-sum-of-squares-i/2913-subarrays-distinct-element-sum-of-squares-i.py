class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        # brute force 
        count = 0
        n = len(nums)
        for i in range(0, n):
            for j in range(i, n):
                arr = nums[i:j+1]
                count += len(set(arr))**2
        return count
