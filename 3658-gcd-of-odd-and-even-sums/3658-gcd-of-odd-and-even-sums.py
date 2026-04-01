class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def findGCD(a, b):
            if a == 0:
                return b
            return findGCD(b % a, a)
        
        odd_sum = 0
        even_sum = 0
        for i in range(1, 2*n + 1 ):
            if i %2 == 0:
                even_sum += i 
            else :
                odd_sum +=i
        return findGCD(odd_sum,even_sum)