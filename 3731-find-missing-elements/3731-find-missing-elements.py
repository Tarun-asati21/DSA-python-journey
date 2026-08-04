class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        low = nums[0]
        high = nums[-1]
        req = []
        for i in range(low, high+1):
            req.append(i)
        
        lst = sorted(list(set(req)-set(nums)))
        return lst