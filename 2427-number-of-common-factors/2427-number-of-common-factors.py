class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        factor1 =[a]
        factor2 = [b]
        for i in range (1, a//2 + 1 ) :
            if a%i == 0 :
                factor1.append(i)
        for i in range(1, b//2 +1) :
            if b%i == 0 :
                factor2.append(i)
        
        return len(set(factor1) & set(factor2))