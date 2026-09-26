class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        freq = {}
        for i, j in knowledge :
            freq[i]=j
        
        ans = ""
        i=0
        while i < len(s) :
            if s[i] == "(" :
                temp = ""
                i+=1
                while True :
                    if s[i] == ")" :
                        i+=1
                        break
                    else :
                        temp += s[i]
                        i+=1
                if temp in freq :
                    ans += freq[temp]
                else :
                    ans += "?"
            else :
                ans += s[i]
                i+=1
        return ans 

                    

                