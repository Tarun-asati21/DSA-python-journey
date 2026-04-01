class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        temp = bin(n)[2:]
        for i in range(len(temp)-1):
            if int(temp[i]) == int(temp[i+1]) :
                return False
            continue
        return  True
