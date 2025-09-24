class Solution:
    def numberOfMatches(self, n: int) -> int:
        sumi=0
        while n :
            if n==1 :
                break
            elif n%2 == 0 :
                n = n/2
                sumi+=n
            else :
                n = (n-1)/2 + 1
                sumi+= n-1
        return int(sumi)