class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        st = set(word)
        lst=[]
        for i in range(26) :
            lower = chr(ord("a") + i)
            upper = chr(ord("A") + i)
            if lower in st and upper in st :
                lst.append(lower)
        if len(lst) == 0 :
            return 0
        ans=0
        for ch in lst :
            for i in range(len(word)) :
                if word[i] == ch.upper() :
                    new = word[i:]
                    if ch in new :
                        break
                    else :
                        ans +=1
                        break
        return ans
