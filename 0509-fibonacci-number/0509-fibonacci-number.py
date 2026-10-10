class Solution:
    def fib(self, n: int) -> int:
        dp = {}
        
        def helper(num):
            if num==0 or num == 1 :
                return num
            
            if num in dp :
                return dp[num]
            
            a1 = helper(num-1)
            a2= helper(num-2)
            ans = a1+a2

            dp[num] = ans
            return ans 
        
        return helper(n)
        