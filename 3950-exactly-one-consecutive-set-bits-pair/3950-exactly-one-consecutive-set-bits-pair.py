class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        temp= bin(n)[2:]
        count=0
        for i in range(1 , len(temp)) :
            if temp[i-1] + temp[i] == "11" :
                count+=1

        return count == 1