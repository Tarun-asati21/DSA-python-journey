class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        suffix_arr = [0]*n 
        suffix_arr[-1] = nums[-1]
        for i in range(n-2, -1, -1) :
            suffix_arr[i] = min(nums[i], suffix_arr[i+1])

        maxi = -float("inf")
        sumi= 0
        for i in range (len(nums)-1) :
            sumi += nums[i]
            mini = suffix_arr[i+1]
            score = sumi - mini
            maxi = max(maxi, score)
        return maxi 
