class Solution:
    def minOperations(self, nums: list[int]) -> int:
        def check_prime(num) :
            if num == 1 :
                return False
            elif num == 2 or num == 3 :
                return True 
            elif num % 2 == 0 :
                return False
            else :
                # check only till root n 
                i = 3
                while i * i <= num:
                    if num % i == 0:
                        return False
                    i += 2
                return True 
        
        def next_prime(n):
            if n <= 2:
                return 2
            if n % 2 == 0:
                n += 1
            while not check_prime(n):
                n += 2
            return n
        
        operations = 0
        for i in range(len(nums)):
            
            # EVEN index → need PRIME
            if i % 2 == 0:
                if not check_prime(nums[i]):
                    p = next_prime(nums[i])
                    operations += (p - nums[i])
            
            # ODD index → need NON-PRIME
            else:
                if check_prime(nums[i]):
                    if nums[i] == 2:
                        operations += 2
                    else:
                        operations += 1
        
        return operations  

            