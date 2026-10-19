class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        if len(nums)%2 != 0 :
            return False
        freq= {}
        for num in nums :
            freq[num] = freq.get(num, 0)+1
        for val in freq.values() :
            if val%2 == 1 :
                return False
        return True