class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # tc = O(n+nlogn)
        freq = {}
        for ch in s :
            freq[ch] = freq.get(ch, 0) + 1

        new = sorted(freq.items()) # dattype : [["a",2],["b",3],["c",1]]

        start = ""
        center = ""
        end = ""
        for lst in new :
            idx = int(lst[1]//2)
            start += lst[0] * idx
            end = (lst[0] * idx) + end
            mid = lst[1] - 2*idx  
            if mid == 0 :
                continue
            else :
                center += lst[0] * mid
        
        return start + center + end
        




