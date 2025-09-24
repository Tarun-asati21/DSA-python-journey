class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            result=""
            for i,letter in enumerate(word):
                if letter == ch :
                    for j in range(i,-1,-1):
                        result+=word[j]
                    break
            
            lst=word.split(ch,1)
            result+=lst[1]
            return result 
        else:
            return word