class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        for i, num in enumerate(nums) :
            if num >= k :
                break
        return len(nums[:i])