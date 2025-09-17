class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """

        maxi=0
        count=0
        stack=[]
        for ch in s :
            if ch=="(":
                stack.append(1)
                count=len(stack)
                maxi=max(count, maxi)
            if ch==")":
                stack.pop()

        return maxi

