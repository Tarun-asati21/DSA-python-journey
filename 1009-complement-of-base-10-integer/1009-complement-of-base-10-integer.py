class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary = bin(n)[2:]
        temp = ""
        for ch in binary :
            if ch == "1" :
                temp += "0"
            else :
                temp += "1"
        return int(temp,2)
