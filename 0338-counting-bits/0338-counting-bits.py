class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1) :
            temp = bin(i)[2:]
            count=0
            for ch in temp :
                if ch=="1":
                    count+=1
            ans.append(count)
        return ans