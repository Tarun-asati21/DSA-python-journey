class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hash = {}
        for ch in sentence :
            if ch in hash :
                hash[ch]+=1
            else :
                hash[ch]=1
        
        return len(hash.keys()) == 26