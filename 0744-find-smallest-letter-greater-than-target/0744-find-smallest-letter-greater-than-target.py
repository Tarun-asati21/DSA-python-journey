class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        t_value = ord(target)
        for i in range(len(letters)):
            value = ord(letters[i])
            if value > t_value :
                return letters[i]
        return letters[0]