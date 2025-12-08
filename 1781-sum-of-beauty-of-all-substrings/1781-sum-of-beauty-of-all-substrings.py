class Solution:
    def beautySum(self, s: str) -> int:
        def hash(string) :
            freq={}
            for i in string :
                if i in freq :
                    freq[i] += 1
                else :
                    freq[i]=1
            beauty = max(freq.values())-min(freq.values())
            return beauty
        
        maxi=0
        sumi=0
        for i in range (0, len(s)):
            for j  in range (i, len(s)):
                sumi += hash(s[i:j+1])
                maxi=max(sumi, maxi)
        return maxi 
