class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        a = nums[0]
        temp = sorted(nums[1:])
        b= temp[0]
        c=temp[1]
        return a+b+c
        
        