class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
    
        search = original
        i=0
        while i < len(nums):
            if nums[i] == search :
                search = 2*search 
                i=0
            else :
                i+=1
        return search
                    