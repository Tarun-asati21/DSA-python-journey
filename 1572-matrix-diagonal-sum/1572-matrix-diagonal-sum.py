class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sumi  = 0
        rows = len(mat)
        columns = len(mat[0])
        for i in range (0,rows) :
            for j in range  (0,columns) :
                if i == j or i+j == rows-1 :
                    sumi += mat[i][j]
        return sumi