class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        ans = 0
        n = len(colors)

        for i in range(n-1, 0, -1) :
            if colors[i] != colors[0] :
                ans = max(ans, i) 
                break

        for i in range(0, n-1) :
            if colors[i] != colors[-1] :
                ans = max(ans, n-1-i) 
                break
        
        return ans 