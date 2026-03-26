class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        arr = []
        for i in range(0, len(grid)-2 ):
            for j in range(0, len(grid)-2):
                
                maxi = 0
                for k in range(i,i+3):
                    for p in range(j, j+3):
                        maxi = max(maxi, grid[k][p])
                arr.append(maxi)

        rows = len(grid)-2
        matrix = []
        for i in range(rows):
            row = arr[i * rows:(i + 1) * rows]
            matrix.append(row)
        return matrix