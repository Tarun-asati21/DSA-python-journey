class Solution:
    def hammingWeight(self, n: int) -> int:
        temp = bin(n)[2:]
        count = 0 
        for ch in temp :
            if ch == "1":
                count+=1
        return count