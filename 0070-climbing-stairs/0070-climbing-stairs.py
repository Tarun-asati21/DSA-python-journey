class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def helper (i, n):
            if i == n :
                return 1
            if i > n :
                return 0
            
            if i in dp :
                return dp[i]
            
            a = helper(i+1, n)
            b = helper(i+2, n)

            ans = a+b
            dp[i] = ans
            return ans
        
        return helper(0, n)