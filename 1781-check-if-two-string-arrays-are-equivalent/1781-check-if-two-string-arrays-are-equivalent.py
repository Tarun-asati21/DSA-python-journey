class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        arr1="".join(word1)
        arr2="".join(word2)
        return arr1==arr2