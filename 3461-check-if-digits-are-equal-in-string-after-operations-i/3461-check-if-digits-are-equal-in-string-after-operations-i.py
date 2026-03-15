class Solution:
    def hasSameDigits(self, s: str) -> bool:
        temp = s
        for i in range(0, len(s)-2):
            new_temp= ""
            for j in range(1, len(temp)):
                ch = int(temp[j]) + int(temp[j-1])
                ch = ch % 10
                new_temp += str(ch)
            temp = new_temp
            if len(temp) == 2:
                if int(temp[0]) == int(temp[1]):
                    return True
                return False