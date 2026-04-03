class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for ch in encoded :
            arr.append(arr[-1]^ch)
        return arr
        