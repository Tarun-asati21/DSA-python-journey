from typing import List

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        
        # function to check prime
        def isPrime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        # count frequency
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # check prime frequency
        for value in freq.values():
            if isPrime(value):
                return True
        
        return False