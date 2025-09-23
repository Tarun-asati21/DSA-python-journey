class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n%2 != 0 :
            lst=[0]
        else :
            lst=[]
        for i in range(1,(n//2 + 1)):
            lst.append(i)
            lst.append(-i)
        return lst 
        
