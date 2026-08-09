class Solution:

    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        def discount(x, n):
            return (x * (100 - n)) / 100

        prices.sort(reverse=True)
        discounts.sort(reverse=True)

        mini = 0
        for i in range(len(prices)):
            if i < len(discounts):
                mini += discount(prices[i], discounts[i])
            else:
                mini += prices[i]
        return mini
       