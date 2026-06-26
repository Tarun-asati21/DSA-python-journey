class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = {"b":0, "a":0,"l" :0,"o":0,"n":0}
        check = ["b","a","l","o","n"]
        for ch in text :
            if ch in check :
                freq[ch] += 1 
            else :
                continue
        
        if freq["b"] == 0 or freq["a"] == 0 or freq["n"] == 0 :
            return 0
        if freq["l"] < 2 or freq["o"] < 2 :
            return 0
        value1 = min(freq["b"],freq["a"],freq["n"])
        value2 = min(freq["l"], freq["o"])
        if value2%2 == 1 :
            value2 -= 1
        if value1 <= value2//2 :
            return value1
        else :
            return value2//2
            