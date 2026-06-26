class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        lst = []
        for num in nums :
            temp = str(num)
            for ch in temp :
                lst.append(int(ch))
        return lst