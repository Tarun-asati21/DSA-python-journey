class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        asc_sum = nums[0]
        desc_sum = 0
        maxi = nums[0]
        for i in range(1, len(nums)) :
            maxi = max(maxi, nums[i])
            if nums[i] >= nums[i-1] :
                asc_sum += nums[i]
            else :
                desc_sum += nums[i]
        
        desc_sum += maxi
        if asc_sum > desc_sum :
            return 0
        elif asc_sum < desc_sum :
            return 1
        else :
            return -1
            
            