class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        maxi=0
        for sen in sentences:
            lst=sen.split()
            maxi=max(maxi,len(lst))
        return maxi