class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}
        for i,ch in enumerate(s) :
            if ch in freq :
                freq[ch] = [freq.get(ch)[0] + 1 , i]
            else :
                freq[ch] = [1, i]
        
        for k,v in freq.items():
            if v[0] == 1 :
                return v[1]
        return -1