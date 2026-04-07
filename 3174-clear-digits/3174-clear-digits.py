class Solution:
    def clearDigits(self, s: str) -> str:
        temp = []
        for ch in s :
            if ch in ["0","1","2","3","4","5","6","7","8","9"] and len(temp) > 0 :
                temp.pop()
            else :
                temp.append(ch)
        return "".join(temp) 