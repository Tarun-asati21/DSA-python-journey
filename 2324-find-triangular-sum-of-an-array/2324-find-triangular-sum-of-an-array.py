class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1 :
            new_nums=[]
            for i in range (0, len(nums)-1):
                add = (nums[i]+ nums[i+1]) % 10
                new_nums.append(add)
            nums = new_nums
        return nums[0]

