class Solution:
    def findComplement(self, num: int) -> int:
        temp = bin(num)[2:]
        ans = ""
        for i in range(len(temp)):
            if temp[i]=="0":
                ans += "1"
            else :
                ans += "0"
        return int(ans,2)

        # tc = 3(O(log num with base 2))