class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        total_slices = 0
        current_chain = 0
        
        for i in range(2, n):
            # Check if the current element maintains the arithmetic progression
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                current_chain += 1
                total_slices += current_chain
            else:
                current_chain = 0
                
        return total_slices