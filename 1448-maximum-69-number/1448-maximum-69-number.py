class Solution:
    def maximum69Number (self, num: int) -> int:
        result = ""
        count=0
        for i in str(num):
            if i == "6" and count == 0 :
                count = 1
                result += "9"
            else :
                result += i
        return int(result)
        