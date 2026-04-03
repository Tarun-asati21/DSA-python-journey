class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def lcp(s1, s2):
            i = 0
            while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
                i += 1
            return s1[:i]

        prefix = strs[0]
        for i in range (1, len(strs)) :
            prefix = lcp(prefix, strs[i])
            if prefix == "":
                return ""
        return prefix
