class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count=0
        row = len(mat)
        column = len(mat[0])
        for i in range(0,row):
            for j in range(0, column):
                if mat[i][j]==1 :
                    # row check
                    temp_row = i 
                    sumi = 0
                    for k in range(0,column):
                        sumi += mat[temp_row][k]
                    sumi_2 = 0
                    # column check
                    temp_col = j
                    for k in range(0, row):
                        sumi_2 += mat[k][temp_col]

                    if sumi==1 and sumi_2==1 :
                        count+=1
        return count                        