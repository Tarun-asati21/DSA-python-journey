class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def GCD(a, b):
            if a == 0:
                return b
            return GCD(b % a, a)
        
        return GCD(min(nums), max(nums))