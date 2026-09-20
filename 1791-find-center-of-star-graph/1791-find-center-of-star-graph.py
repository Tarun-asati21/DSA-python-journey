class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        # array brute force coming to my mind is at first instant :
        arr = edges[0]  + edges[1]
        freq={}
        for num in arr :
            freq[num] = freq.get(num,0)+1
        for k,v in freq.items() :
            if v == 2 :
                return k