class Solution:
    def reverseBits(self, n: int) -> int:
        temp = bin(n)[2:].zfill(32)
        rev = temp[::-1]
        return int(rev, 2)