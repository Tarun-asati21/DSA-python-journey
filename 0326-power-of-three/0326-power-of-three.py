class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<0 :
            return False
        else :
            while n :
                if n == 1 :
                    return True
                if (n >0 and n <1)  :
                    return False
                n = n/3
            return False
    
        
