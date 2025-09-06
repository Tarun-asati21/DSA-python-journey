class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0 :

            reverse_x= int(str(x)[::-1])
            if reverse_x == x :
                return True 
            else :
                return False

        if x< 0 :
            return False