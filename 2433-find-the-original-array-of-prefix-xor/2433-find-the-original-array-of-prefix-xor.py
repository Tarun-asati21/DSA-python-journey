class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]]
        xori = pref[0]
        curr = pref[0]
        for num in pref[1:] :
            xori ^= num
            arr.append(xori)
            curr ^= arr[-1]
            xori = curr
        return arr
