class Solution:
    def isHappy(self, n: int) -> bool:
        temp = str(n)
        if temp == "1" :
            return True
        
        while int(temp) > 1 :
            result = 0 
            for ch in temp :
                result += int(ch)**2
            temp = str(result)
            if temp == "1" :
                return True
            if temp in {"2","3","4","5","6","8","9"} :
                return False
        