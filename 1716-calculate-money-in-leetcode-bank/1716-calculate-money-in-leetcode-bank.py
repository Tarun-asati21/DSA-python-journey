class Solution:
    def totalMoney(self, n: int) -> int:
        week = 0
        day = 0
        total = 0
        for i in range(n):
            total += week + day + 1
            day += 1
            if day == 7:
                day = 0
                week += 1
        return total
        