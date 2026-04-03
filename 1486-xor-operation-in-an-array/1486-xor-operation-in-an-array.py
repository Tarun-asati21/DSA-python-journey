class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range (0, n ):
            nums.append(start+2*i)

        x = nums[0]
        for num in nums[1:] :
            x^=num
        return x
