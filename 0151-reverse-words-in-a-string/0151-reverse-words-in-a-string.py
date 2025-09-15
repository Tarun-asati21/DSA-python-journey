class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        words=s.split()
        size= len(words)
        result=""
        for i in range(size-1,-1,-1):
            result += words[i]+" "

        return result.strip()