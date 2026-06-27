class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        temp = []
        for i in range(len(nums)-1,-1,-1):
            temp.append(nums[i])
        return nums+temp