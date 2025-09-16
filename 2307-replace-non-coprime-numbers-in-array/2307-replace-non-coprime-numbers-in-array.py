
class Solution(object):
    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # def hcf(x,y):

        #     factors_x =[]
        #     i=1
        #     while i <= x :
        #         if x%i == 0 :
        #             factors_x.append(i)
        #         i+=1

        #     factors_y=[]
        #     j=1
        #     while j<=y :
        #         if y%j == 0 :
        #             factors_y.append(j)
        #         j+=1

        #     common_factors = set(factors_x) & set(factors_y)
        #     return max(common_factors)

        # if len(nums)==1 :
        #     return nums
        # l=0
        # r=1
        # while r<len(nums) :
        #     high = hcf(nums[l],nums[r])
        #     if  high > 1 :
        #         low = (nums[l]*nums[r])//high
        #         del nums[l:r+1]
        #         nums.insert(l, low)
        #     else :
        #         l+=1
        #         r+=1
        # return nums

        # def gcd(x,y):

        #     factors_x =[]
        #     i=1
        #     while i <= x :
        #         if x%i == 0 :
        #             factors_x.append(i)
        #         i+=1

        #     factors_y=[]
        #     j=1
        #     while j<=y :
        #         if y%j == 0 :
        #             factors_y.append(j)
        #         j+=1

        #     common_factors = set(factors_x) & set(factors_y)
        #     return max(common_factors)
                   
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        stack = []
        for num in nums:
            stack.append(num)
            # keep merging as long as top 2 are non-coprime
            while len(stack) > 1:
                a, b = stack[-2], stack[-1]
                g = gcd(a, b)
                if g > 1:  # non-coprime
                    lcm = (a * b) // g
                    stack.pop()
                    stack.pop()
                    stack.append(lcm)
                else:
                    break
                    
        return stack