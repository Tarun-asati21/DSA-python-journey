class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k) :
            mini = min(nums)
            for j in range(len(nums)) :
                if nums[j] == mini :
                    nums[j] = multiplier * mini
                    break 
        return nums