class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        count= len(prices)
        length = 1
        for i in range(1,len(prices)):
            if prices[i-1]-prices[i] == 1 :
                length += 1 
            else :
                if length != 1 :
                    count += ((length**2)-(length))/2
                length = 1

        # edge case
        if length != 1 :
            count += ((length**2)-(length))/2
            
        return int(count)   