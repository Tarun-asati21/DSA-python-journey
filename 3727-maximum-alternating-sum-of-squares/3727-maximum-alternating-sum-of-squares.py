class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        lst = [abs(num) for num in nums]
        lst.sort()
        req = len(lst)//2
        temp1 = lst[ : req]
        temp2 = lst[req:]
        small = 0
        large = 0
        for num in temp1 :
                small += num**2
        for num in temp2 :
                large += num**2
        return large - small
