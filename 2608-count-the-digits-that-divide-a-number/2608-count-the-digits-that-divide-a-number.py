class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count=0
        for i in str(num):
            if int(num) % int(i) == 0:
                count+=1
        return count