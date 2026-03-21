class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if len(original) != m*n :
            return []

        arr = [[0]*n for _ in range(m)] 

        count = 0 
        for i in range (0,m):
            arr[i] = original[count : count+n ]
            count+=n
        return arr