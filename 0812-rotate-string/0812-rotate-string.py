class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        
        for i, ch in enumerate(s) :
            shifted_s = s[i+1:]+s[:i+1]
            if shifted_s == goal :
                return True 
        return False