class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # # brute force approach -> time limit exceeded
        # lst=[0]
        # for j in range (0, len(prices)):
        #         sell = max(prices[j:])
        #         if j==0 :
        #             buy = prices[j]
        #         else :
        #             buy = min(prices[:j])
        #         pnl = sell-buy
        #         if pnl > 0 :
        #             lst.append(pnl)
        # return max(lst)

        # 2 pointer approach
        left = 0
        right = 1
        max_p = 0
        while right < len(prices):
            profit = prices[right]-prices[left]
            if prices[right]>prices[left]:
                max_p=max(max_p, profit)
            else :
                left=right 
            right+=1
        
        return max_p
       