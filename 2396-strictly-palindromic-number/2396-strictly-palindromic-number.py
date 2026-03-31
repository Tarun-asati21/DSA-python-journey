class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def binary(num, base):
            if num == 0 :
                return "0"
            binary_num = ""
            while num > 0 :
                rem = num % base
                binary_num = str(rem) + binary_num
                num = num//base
            return binary_num
        
        for i in range(2, n-2+1):
            temp = binary(n, i)
            if temp ==  temp[::-1]:
                continue
            return False
        return True