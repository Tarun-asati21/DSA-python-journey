class Solution:
    def minRotations(self, s: str) -> int:
        rot = 0
        prev = "0"
        for ch in s :
            a=abs(int(ch)-int(prev))
            b= abs(10-a)
            rot += min(a,b)
            prev = ch
        return rot
