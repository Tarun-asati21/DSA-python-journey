class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        from heapq import heappush,heappop,heapify
        max_heap=[]
        for i in dimensions :
            heappush(max_heap, (-(i[0]**2 + i[1]**2), -(i[0]*i[1])) )
        return -heappop(max_heap)[1]