class Solution:
    def convertToBase7(self, num: int) -> str:
        n=abs(num)
        if n == 0:
            return "0"
        
        res = ""
        while n > 0:
            res = str(n % 7) + res
            n //= 7
        if num > 0 :
            return res
        else :
            return "-" + res