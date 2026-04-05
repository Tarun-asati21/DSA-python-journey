class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        temp = 0
        for i in range(0, len(nums)) :
            arr = [int(ch) for ch in str(nums[i])]
            if sum(arr) == i :
                return i 
        return -1