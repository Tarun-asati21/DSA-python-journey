class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        mini=float("inf")
        for i in range(0 , len(nums)):
            if nums[i] == 1 :
                for j in range(len(nums)) :
                    if nums[j] == 2 :
                        diff = abs(i-j)
                        mini = min(mini, diff)
        if mini != float("inf") :
            return mini
        return -1
            