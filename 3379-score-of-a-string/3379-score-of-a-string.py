class Solution:
    def scoreOfString(self, s: str) -> int:
        l=0
        r=1
        lst=[]
        while r<len(s) :
            diff=abs(ord(s[l])-ord(s[r]))
            lst.append(diff)
            l+=1
            r+=1
        return sum(lst)
        
