class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        lst=[]
        for i, num in enumerate(nums):
            if num > target :
                break
            elif num == target :
                lst.append(i)
            else :
                continue
        return lst