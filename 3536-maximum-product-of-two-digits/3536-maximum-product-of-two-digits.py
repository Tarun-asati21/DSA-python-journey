class Solution:
    def maxProduct(self, n: int) -> int:
        temp = str(n)
        lst=[]
        for ch in temp :
            lst.append(ch)

        lst2= []
        for ch in lst :
            lst2.append(int(ch))

        lst2.sort()
        return lst2[-1]*lst2[-2]
                

