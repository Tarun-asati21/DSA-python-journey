class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        lst = [0]
        for i in range (0, len(gain)):
            lst.append(lst[-1]+gain[i])
        return max(lst)