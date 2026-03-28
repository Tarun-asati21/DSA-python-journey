class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums = sorted(nums)
        arr =[]
        l=0
        r=len(nums)-1
        while l <= r :
            arr.append((nums[l]+nums[r])/2)
            l+=1
            r-=1
        return min(arr)