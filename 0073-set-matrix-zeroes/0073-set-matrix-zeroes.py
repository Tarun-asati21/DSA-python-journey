class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lst=[]
        row = len(matrix)
        column = len(matrix[0])
        for i in range (0, row):
            for j in range(0, column) :
                if matrix[i][j] == 0 :
                    lst.append([i,j])

        for i in range(0, len(lst)):
            zero_row=lst[i][0]
            zero_column=lst[i][1]

            for j in range(0, row) :
                matrix[j][zero_column]=0
            for j in range (0, column) :
                matrix[zero_row][j]=0
        
        return matrix