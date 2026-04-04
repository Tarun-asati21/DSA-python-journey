class Solution:
    def checkString(self, s: str) -> bool:
        a = 0
        b = 0
        for ch in s :
            if ch == "a" :
                a += 1
            if ch == "b" :
                break 
        arr = ["b"]*(len(s)-a)
        temp = "".join(arr)
        return temp == s[a:]