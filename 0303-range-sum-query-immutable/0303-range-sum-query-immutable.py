class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        nums = self.nums
        temp=nums[left:right+1]
        return sum(temp)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)