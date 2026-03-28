class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        temp=""
        for i in range(k-1, -1, -1):
            temp+=s[i]
        return temp + s[k:]