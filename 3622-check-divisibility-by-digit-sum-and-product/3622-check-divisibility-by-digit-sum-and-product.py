class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sumi = 0
        prod = 1
        temp = str(n)
        for ch in temp :
            sumi+=int(ch)
            prod*= int(ch)
        if n % (sumi + prod) == 0 :
            return True
        return False