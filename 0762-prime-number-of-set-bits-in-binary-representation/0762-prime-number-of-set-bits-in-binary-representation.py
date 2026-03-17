class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        temp=0
        for i in range(left, right+1):
            binary = bin(i)[2:]
            count= 0
            for ch in str(binary):
                if ch == "1":
                    count += 1
            factor = 0
            for j in range(1, count + 1):
                if factor > 2 :
                    break
                if factor == 1  and j > count//2 + 1 :
                    factor += 1
                    break
                if count%j == 0 :
                    factor += 1
            if factor == 2 :
                temp +=1
        return temp