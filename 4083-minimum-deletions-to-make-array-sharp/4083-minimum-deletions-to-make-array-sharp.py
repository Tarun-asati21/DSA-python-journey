class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(0, n-1):
            if nums[i] == nums[i+1] :
                count+=1
        return count