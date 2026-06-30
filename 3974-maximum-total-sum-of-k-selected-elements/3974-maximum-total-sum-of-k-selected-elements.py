class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        
        new_arr = sorted(nums, reverse=True)
        choosen_elements = new_arr[:k]
        sumi = 0
        for i in choosen_elements :
            if i >= (i*mul) :
                sumi += i 
            else :
                sumi += (i*mul)
                mul-=1
        return sumi

