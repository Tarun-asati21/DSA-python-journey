class Solution:
    def maxDepth(self, s: str) -> int:
        maxi = -float("inf")
        stack = []
        for ch in s :
            if ch == "(" :
                stack.append(ch)
            elif ch == ")" :
                length = len(stack)
                maxi = max(maxi, length)
                stack.pop()
            else :
                continue
        return maxi if maxi != -float("inf") else 0
        