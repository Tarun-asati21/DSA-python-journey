class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:

        n = len(nums)
        pre = []
        suff = [0]*n
        count = 0
        prefix = 0
        suffix = 0
        for i in range(n):
            prefix += nums[i]
            pre.append(prefix)
        for i in range(n-1, -1, -1) :
            suffix += nums[i]
            suff[i] = suffix
        count = 0
        for i in range(n-1) :
            if pre[i] >= suff[i+1] :
                count+=1
        return count