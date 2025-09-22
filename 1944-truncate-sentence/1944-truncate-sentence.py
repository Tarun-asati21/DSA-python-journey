class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result=""
        for ch in s.split()[:k]:
            result= result + ch + " "
        return result.strip()