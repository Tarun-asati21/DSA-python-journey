class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        if len(nums) < 3 :
            return nums

        ans = [nums[0]]
        for i in range(1, len(nums)-1) :
            if nums[i] > max(nums[:i]) :
                ans.append(nums[i])
            elif nums[i] > max(nums[i+1:]) :
                ans.append(nums[i])
            else :
                continue
            
        ans.append(nums[-1])
        return ans

