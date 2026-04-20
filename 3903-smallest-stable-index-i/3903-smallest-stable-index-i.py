class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(0, len(nums)) :
            score = max(nums[:i+1]) - min(nums[i:])
            if score <= k :
                return i
        return -1
         