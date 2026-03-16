class Solution:
    def smallestNumber(self, n: int) -> int:
        while True :
            temp = bin(n)[2:]
            if set(temp)=={"1"}:
                return n
            n+=1
        