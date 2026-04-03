class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        temp = bin(n)[2:]
        idx = 0
        even = 0
        odd = 0
        for i in range (len(temp)-1, -1, -1 ):
            if idx%2 == 0 and temp[i] == "1" :
                even += 1
                idx +=1
                continue
            if idx%2 == 1 and temp[i] == "1" :
                odd += 1
                idx+=1
                continue
            idx+=1
        return [even, odd]