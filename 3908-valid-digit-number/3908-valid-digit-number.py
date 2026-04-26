class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        temp = str(n) 
        check = str(x)
        if temp[0] == check :
            return False
        for ch in temp :
            if ch == check :
                return True
        return False