class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def pro(n,t):
            temp=str(n)
            ans=1
            for dig in temp :
                ans*=int(dig)
            return ans%t==0

        temp=n
        div=t
        while pro(temp, div) != True :
            temp+=1
        return temp
