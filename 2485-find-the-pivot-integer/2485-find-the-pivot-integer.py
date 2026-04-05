class Solution:
    def pivotInteger(self, n: int) -> int:
        # brute force 
        arr=[]
        for i in  range(1, n+1) :
            arr.append(i)
        for j in range(0, len(arr)):
            if sum(arr[:j+1]) == sum(arr[j:]) :
                return j+1
        return -1