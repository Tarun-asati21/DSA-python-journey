class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # # brute force - TC = O(n**2)
        # ans = 0 
        # for i in range (0, len(colors)) :
        #     for j in range (i+1, len(colors)) :
        #         if colors[i] != colors[j] :
        #             ans = max(ans, abs(i-j))
        # return ans 

        # TC = O(n)
        n =len(colors)
        ans = 0

        for i in range(n-1, 0, -1) :
            if colors[0] != colors[i] :
                ans = max(ans, i)
                break
        
        for i in range(n-1) :
            if colors[-1] != colors[i] :
                ans = max(ans, n-1-i)
                break
        
        return ans 
        

