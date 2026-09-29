class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n=len(nums)
        maxi = -float("inf")
        pre = 1
        suff = 1
        for i in range(n):
            pre *= nums[i]
            suff *= nums[n-i-1]
            maxi = max(maxi, pre , suff)
            if suff == 0 :
                suff = 1
            if pre == 0 :
                pre = 1
        return maxi