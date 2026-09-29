class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.prefix_arr = [0] * (len(nums))
        temp=0
        for i in range(0, len(nums)) :
            temp += nums[i]
            self.prefix_arr[i] = temp

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_arr[right]
        return self.prefix_arr[right] - self.prefix_arr[left-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)