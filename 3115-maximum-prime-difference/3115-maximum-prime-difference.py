class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def is_prime(n) :
            if n==1 :
                return False
            elif n==2 or n==3 :
                return True
            elif n%2 == 0 :
                return False
            else :
                for i in range(2, int(n*0.5)+1) :
                    if n%i == 0 :
                        return False 
                return True
        
        index  = []
        for i in range(0, len(nums)) :
            if is_prime(nums[i]) :
                index.append(i)
        return abs(index[-1] - index[0])