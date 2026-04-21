class Solution:
    def countKeyChanges(self, s: str) -> int:
        if len(s) == 1 :
            return 0
        s =  s.lower()
        ans = 0
        for i in range (1, len(s)):
            if s[i] != s[i-1] :
                ans +=1
        return ans
