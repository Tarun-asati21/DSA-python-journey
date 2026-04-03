class Solution:
    def reverseWords(self, s: str) -> str:
        final_ans = ""
        temp = ""
        
        i = len(s) - 1
        
        while i >= 0:
            if s[i] == " ":
                i -= 1
                continue
            
            temp = ""
            while i >= 0 and s[i] != " ":
                temp = s[i] + temp
                i -= 1
            
            if final_ans:
                final_ans += " "
            final_ans += temp
        
        return final_ans