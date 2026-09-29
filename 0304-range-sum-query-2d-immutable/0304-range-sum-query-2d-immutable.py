class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        n = len(matrix)
        m = len(matrix[0]) if n else 0
        self.ps = [[0]*(m+1) for _ in range(n+1)] # prefix sum matrix
        for i in range(n):
            row_ps = self.ps[i+1]
            for j in range(m):
                row_ps[j+1] = matrix[i][j] + self.ps[i][j+1] + row_ps[j] - self.ps[i][j]
                # (Current cell) + (Top rectangle) + (Left rectangle) - (Top left rectangle)
 

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ps = self.ps
        return ps[row2+1][col2+1] - ps[row1][col2+1] - ps[row2+1][col1] + ps[row1][col1]
        # Total − Top − Left + Overlap
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)