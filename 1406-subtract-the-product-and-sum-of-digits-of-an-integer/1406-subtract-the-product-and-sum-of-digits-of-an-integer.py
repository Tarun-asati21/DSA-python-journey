class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        pro=1
        sumi=0
        for i in str(n):
            pro*=int(i)
            sumi+=int(i)
        return pro-sumi