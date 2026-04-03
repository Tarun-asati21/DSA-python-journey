class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        freq = {}
        for num in nums :
            if num in freq :
                freq[num]+=1
            else :
                freq[num]=1
        
        xor = 0
        for key, value in freq.items() :
            if value == 2 :
                xor^=key
        return xor 