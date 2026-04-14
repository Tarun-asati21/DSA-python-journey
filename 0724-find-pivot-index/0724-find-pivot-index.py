class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # # brute force 
        # for i in range(len(nums)) :
        #     if sum(nums[:i]) == sum(nums[i+1:]) :
        #         return i 
        # return -1

        # # better
        # pre = [0] * len(nums)
        # for i in range (1, len(nums)) :
        #     pre[i] = nums[i-1] + pre[i-1]

        # suff = [0] * len(nums)
        # for i in range(len(nums)-2, -1, -1):
        #     suff[i] = nums[i+1] +  suff[i+1]
        
        # for  i in range(len(nums)) :
        #     if pre[i] == suff[i] :
        #         return i 
        #         break
        # return -1

        # optimal 
        sumi = sum(nums)
        left = 0
        for i in range(len(nums)) :
            if left == sumi - left - nums[i] :
                return i
            left += nums[i]
        return -1 