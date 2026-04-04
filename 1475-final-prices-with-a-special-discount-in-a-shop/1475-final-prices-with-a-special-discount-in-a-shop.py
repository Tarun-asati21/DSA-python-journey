class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        arr = []
        for i in range(len(prices)) :
            temp=1
            for j in range (i+1, len(prices)) :
                if prices[j] <= prices[i] :
                    buy_price = prices[i]
                    discount = prices[j]
                    arr.append(buy_price-discount)
                    temp=0
                    break
            if temp == 1  :
                arr.append(prices[i])
        return arr