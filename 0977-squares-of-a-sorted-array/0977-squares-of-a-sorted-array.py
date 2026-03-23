class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            sq = nums[i]**2
            nums[i] = sq
        return sorted(nums)