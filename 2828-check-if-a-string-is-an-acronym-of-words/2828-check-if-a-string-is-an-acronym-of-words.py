class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        temp =""
        for ch in words :
            temp += ch[0]
        return temp ==  s