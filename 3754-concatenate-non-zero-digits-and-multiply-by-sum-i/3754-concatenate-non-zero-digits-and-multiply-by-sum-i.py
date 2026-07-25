class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        temp=str(n)
        num = ""
        for ch in temp :
            if int(ch) != 0 :
                num += ch
            else :
                continue
        
        sumi=0
        for ch in num :
            sumi+=int(ch)
        return sumi*int(num)
        
