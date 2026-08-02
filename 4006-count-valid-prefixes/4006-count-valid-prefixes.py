class Solution:
    def countValidPrefixes(self, s: str) -> int:
        freq= {}
        valid = 0
        count=0
        for ch in s :
            freq[ch] = freq.get(ch,0)+1
            count+=1
            if count%2 == 1 :
                if abs(freq.get("0",0) - freq.get("1",0) ) == 1 :
                    valid += 1
            elif count%2 == 0 :
                if freq.get("0",0)  == freq.get("1",0)  :
                    valid += 1
            else :
                continue
        return valid



