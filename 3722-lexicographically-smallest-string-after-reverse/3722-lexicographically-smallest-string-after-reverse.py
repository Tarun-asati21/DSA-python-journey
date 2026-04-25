class Solution:
    def lexSmallest(self, s: str) -> str:
        # TC = O(n^2)
        n = len(s)
        mini = s
        for k in range (1, n+1 ) :
            temp1 = s[:k][::-1] + s[k:]
            temp2 = s[:k-1] + s[k-1:][::-1]
            mini = min(mini, temp1, temp2)
        return mini