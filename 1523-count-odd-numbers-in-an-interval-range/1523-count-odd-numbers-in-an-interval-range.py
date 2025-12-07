class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        # brute force -> TLE 
        # count = 0
        # for i in  range(low, high+1):
        #     if i%2 != 0 :
        #         count+=1
        # return count

        # if low%2 != 0 and high%2 != 0 :
        #     return (high-low)//2 + 1
        if low%2 == 0 and high%2 == 0 :
            return (high-low)//2 
        else :
            return (high-low)//2 + 1