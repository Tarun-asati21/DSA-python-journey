class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        sumi =0 
        for i in range(0, len(nums)):
            if i%2==0:
                sumi+=nums[i]
            else:
                sumi-=nums[i]
        return sumi