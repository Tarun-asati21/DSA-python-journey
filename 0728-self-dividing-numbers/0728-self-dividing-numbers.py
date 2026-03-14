class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def helper(num):
            temp = str(num)
            for ch in temp :
                if ch == "0" :
                    return False
                else :
                    ans = num % int(ch)
                    if ans != 0 :
                        return False
            return True    
            
        lst=[]
        for i in range(left, right+1):
            if helper(i) == True :
                lst.append(i)
           
        return lst
                