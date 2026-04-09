class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans=[]
        for word in words :
            count = 0
            for ch in words :
                if word in ch :
                    count+=1
                if count >= 2 :
                    ans.append(word)
                    break
        return ans
