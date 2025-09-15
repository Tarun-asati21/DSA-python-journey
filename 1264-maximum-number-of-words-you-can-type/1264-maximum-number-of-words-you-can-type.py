class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        
        remove_broke = "".join('*' if c in brokenLetters else c for c in text)
        words1 = text.split()
        words2= remove_broke.split()

        count=0
        for w1,w2 in zip(words1,words2):
            if w1==w2 :
                count+=1
        return count
            