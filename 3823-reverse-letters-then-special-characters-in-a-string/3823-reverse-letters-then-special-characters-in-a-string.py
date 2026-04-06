class Solution:
    def reverseByType(self, s: str) -> str:
        letter_arr = []
        special_arr = []
        ans = ""

        for ch in s:
            if ord('a') <= ord(ch) <= ord('z'):
                letter_arr.append(ch)
            else:
                special_arr.append(ch)

        for ch in s:
            if ord('a') <= ord(ch) <= ord('z'):
                ans += letter_arr[-1]
                letter_arr.pop()
            else:
                ans += special_arr[-1]
                special_arr.pop()

        return ans
