class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high+1) :
            if  len(str(i)) % 2 == 1 :
                continue 
            n = len(str(i))//2
            n1= str(i)[:n]
            n2= str(i)[n:]
            sumi1=0
            sumi2=0
            for j in range(0, n):
                sumi1 += int(n1[j])
                sumi2 +=  int(n2[j])
            if sumi1 == sumi2 :
                count+=1
        return count