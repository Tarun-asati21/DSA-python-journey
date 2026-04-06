class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        dict = defaultdict(int)
        limit = int(n**(1/3))
        arr=[]

        for i in range (1, limit+1) :
            i3 = i*i*i
            for j in range (i, limit +1) :
                s = i3 + (j*j*j)
                if s > n :
                    break
                dict[s] += 1 

        for k, v in dict.items() :
            if v >= 2 :
                arr.append(k)

        return sorted(arr)
                