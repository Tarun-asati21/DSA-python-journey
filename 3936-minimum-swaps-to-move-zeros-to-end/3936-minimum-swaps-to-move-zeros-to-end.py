class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        count = 0
        l=0
        r=len(nums)-1
        while l < r :
            if nums[r] == 0 :
                r-=1
                continue
            if nums[l] == 0 :
                nums[l], nums[r] = nums[r],nums[l]
                r-=1
                l+=1
                count+=1
                continue
            l+=1
        return count