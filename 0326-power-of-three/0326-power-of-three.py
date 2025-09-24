class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # # brute force -> maine socha -> while loop pura last tak jaake divide karke check kar raha hai, har no ke liye -> tc badi
        # if n<0 :
        #     return False
        # else :
        #     while n :
        #         if n == 1 :
        #             return True
        #         if (n >0 and n <1)  :
        #             return False
        #         n = n/3
        #     return False

        # better solution -> while loop jo no divisible by 3 hai, unnhi ke liye check kare -> search space choti -> tc choti
        if n<=0 :
            return False
        while n%3 == 0:
            n//=3
        return n==1
    