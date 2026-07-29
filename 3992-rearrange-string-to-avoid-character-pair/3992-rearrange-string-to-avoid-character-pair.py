class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        freq = {}
        for ch in s :
            freq[ch] = freq.get(ch,0) + 1

        ans = ""
        before = ""
        after = ""
        for key,value in freq.items() :
            if key == x :
                after += key*value
            elif key == y :
                before += key*value
            else :
                ans += key*value
        return ans + before + after