class Solution:
    def binaryGap(self, n: int) -> int:
        # convert a no into its binary
        def bin(num) :
            if num == 0 :
                return 0
            temp = ""
            while num >0 :
                rem = num%2
                temp = str(rem)+temp
                num = num //2
            return temp

        b = bin(n)
        maxi = 0
        last = -1        # index of previous '1'

        for i in range(len(b)):
            if b[i] == '1':
                if last != -1:
                    maxi = max(maxi, i - last)
                last = i
                
        return maxi