class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n==1 :
            return True
        elif n<=0:
            return False
        else :
            while n%2 ==0 :
                n/=2
            return n==1
            
