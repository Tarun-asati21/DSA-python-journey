class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000 :
            return 0
        else :
            ans = 0
            for num in range(1000, n+1) :
                ans += num%3
            if n%3==2 :
                return ans-1
            else :
                return ans