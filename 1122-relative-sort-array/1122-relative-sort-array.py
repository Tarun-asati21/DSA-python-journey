class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        freq={}
        arr3=[]
        for num in arr1 :
            if num in arr2 :
                freq[num] = freq.get(num, 0) + 1
            else :
                arr3.append(num)
        arr3.sort()
        
        lst = []
        for num in arr2 :
            val = freq[num]
            for _ in range( val) :
                lst.append(num)

        return lst + arr3