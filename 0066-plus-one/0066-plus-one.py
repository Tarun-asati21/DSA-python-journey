class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for ch in digits :
            num = num + str(ch)
        new =  str(int(num) + 1 )
        
        arr = []
        for i in range (0, len(new)) :
            arr.append(int(new[i]))

        return arr