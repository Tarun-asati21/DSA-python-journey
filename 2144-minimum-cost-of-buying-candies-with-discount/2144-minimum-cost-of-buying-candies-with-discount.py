class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) < 3 :
            return sum(cost)
        lst = sorted(cost)
        pay = 0 
        for i in range(len(lst)-1, -1, -3):
            if i == 0 :
                pay += lst[i]
            else :
                pay += lst[i] + lst[i-1]
        return pay
            