class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = []
        consonant = []
        for ch in s :
            if ch in ["a","e","i","o","u","A","E","I","O","U"] :
                vowel.append(ch)
            else :
                consonant.append(ch)
        
        ans  = ""
        for ch in s :
            if ch in ["a","e","i","o","u","A","E","I","O","U"]  :
                ans += vowel[-1]
                vowel.pop(-1)
            else :
                ans += consonant[0]
                consonant.pop(0)
        return ans
