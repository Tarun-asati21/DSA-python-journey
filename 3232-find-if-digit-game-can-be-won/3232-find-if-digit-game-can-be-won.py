class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        alice = 0
        bob = 0
        for num in nums :
            if num < 10 :
                alice += num
            else :
                bob += num 
        if alice > bob :
            return True 

        alice2 =0 
        bob2 = 0
        for num in nums :
            if num > 9 and num < 100 :
                alice2 += num 
            else :
                bob2 += num 
        if alice2 > bob2 :
            return True 
        
        return False 
            