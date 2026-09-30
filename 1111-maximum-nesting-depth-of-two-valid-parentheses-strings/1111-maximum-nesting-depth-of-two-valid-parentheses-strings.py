class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        depth = 0
        ans = []
        for s in seq :
            if s=="(":
                depth+=1
                ans.append(depth%2)
            else :
                ans.append(depth%2)
                depth-=1
        return ans
