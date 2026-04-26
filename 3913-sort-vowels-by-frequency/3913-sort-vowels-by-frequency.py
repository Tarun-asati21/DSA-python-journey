class Solution:
    def sortVowels(self, s: str) -> str:
        freq = {}
        first_pos = {}
        for i, ch in enumerate(s):
            if ch in "aeiou":
                if ch not in freq:
                    freq[ch] = 0
                    first_pos[ch] = i
                freq[ch] += 1
        sorted_vowels = sorted(freq.keys(), key=lambda x: (-freq[x], first_pos[x]))

        vowels_sorted = []
        for ch in sorted_vowels:
            vowels_sorted.extend([ch] * freq[ch])

        res = list(s)
        idx = 0
        for i in range(len(s)):
            if s[i] in "aeiou":
                res[i] = vowels_sorted[idx]
                idx += 1

        return "".join(res)