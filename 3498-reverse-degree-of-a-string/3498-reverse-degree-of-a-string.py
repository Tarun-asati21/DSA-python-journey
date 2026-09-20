class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i in range(0, len(s)):
            ans += (123 - ord(s[i]))*(i+1)
        return ans
        