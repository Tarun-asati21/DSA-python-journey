class Solution:
    def maxDistinct(self, s: str) -> int:
        # # brute force 
        # sub={}
        # for ch in s :
        #     if ch in sub :
        #         sub[ch]+=1
        #     else :
        #         sub[ch]=1
        # val=0
        # for key in sub :
        #     val+=1
        # return val

        # one line solution 
        return len(set(s))