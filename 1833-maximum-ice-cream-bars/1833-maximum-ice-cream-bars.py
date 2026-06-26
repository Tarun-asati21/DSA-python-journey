class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        if costs[0] > coins :
            return 0
        count = 0
        remaining = coins
        for cost in costs :
            remaining -= cost
            if remaining < 0 :
                return count
            count += 1
        return count