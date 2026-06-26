class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        temp = ""
        for word in words :
            weight = 0
            for ch in word :
                idx = ord(ch) % 97
                weight += weights[idx]
            track = weight % 26 
            temp += (chr(122 - track))
        return temp