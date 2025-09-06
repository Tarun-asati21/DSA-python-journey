class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x >= 0 :
            reverse_no = int(str(x)[::-1])
        else :
            reverse_no = int("-"+str(x)[:0:-1])
        
        if reverse_no < -2**31 or reverse_no > 2**31 - 1:
            return 0
            
        return reverse_no
        