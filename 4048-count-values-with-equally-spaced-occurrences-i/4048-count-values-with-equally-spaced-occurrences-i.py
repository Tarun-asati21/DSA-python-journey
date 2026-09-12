class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        freq = {}
        for i,num in enumerate(nums):
            if num in freq :
                freq[num] = freq.get(num) + [i]
            else :
                freq[num] = [i]
        
        ans = 0
        for key, value in freq.items():
            if len(value) != 3 :
                continue
            if value[1]-value[0] == value[2]-value[1] :
                ans+=1
        return ans