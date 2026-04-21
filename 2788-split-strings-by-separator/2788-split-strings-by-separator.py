class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        final = []
        for ch in words :
            char = ch.split(separator)
            for kom in char :
                if  kom != "" :
                    final.append(kom)
        return final
