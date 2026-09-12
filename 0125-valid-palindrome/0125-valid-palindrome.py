class Solution:
    def isPalindrome(self, s: str) -> str:
        cleaned_text = ""
        for ch in s :
            if ch.isalnum() : # inbuilt function to check that the str is alpha-numeric or not
                cleaned_text+= ch
        return cleaned_text.lower() == cleaned_text.lower()[::-1]