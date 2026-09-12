class Solution:
    def isPalindromic(self, s: str) -> str:
        req_str = ""
        for ch in s :
            num = ord(ch)
            b8 = f"{num:08b}"
            req_str += b8
        return req_str == req_str[::-1]