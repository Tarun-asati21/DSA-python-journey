class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitSum = 0
        sqsum =0
        temp1 = str(n)
        for ch in temp1 :
            digitSum += int(ch)
            sqsum += int(ch)**2
        
        return sqsum - digitSum >= 50
        
        