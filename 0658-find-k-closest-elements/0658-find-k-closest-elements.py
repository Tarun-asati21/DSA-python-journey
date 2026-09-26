from collections import Counter

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        freq = {}
        count = Counter(arr)
        for num in arr :
            dist = abs(num-x)
            freq[num] = dist
        
        freq = dict(sorted(freq.items(), key = lambda item : (item[1], item[0])))
        new_arr=[]
        for key in freq.keys() :
            times = count[key]
            new_arr.extend([key]*times)
        new_arr = new_arr[:k]
        new_arr.sort()
        return new_arr