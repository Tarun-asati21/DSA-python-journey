class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for char in string.punctuation :
            paragraph =  paragraph.replace(char, " ")
        
        paragraph = paragraph.lower().split()
        
        freq = {}
        banned_set = set(banned)
        
        for word in paragraph:
            if word not in banned_set:
                freq[word] = freq.get(word, 0) + 1
        
        return max(freq, key=freq.get)