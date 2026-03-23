class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        # # brute force = TLE
        # m, n = len(grid), len(grid[0])
        # count = 0
        # for i in range(m):
        #     for j in range(n):

        #         count_x=0
        #         count_y=0
        #         for x in range(i+1):
        #             for y in range(j+1):
        #                 if grid[x][y]=="X" :
        #                     count_x +=1
        #                 elif grid[x][y] =="Y":
        #                     count_y +=1
        #                 else:
        #                     continue
        #         if count_x >= 1 and count_x==count_y:
        #             count+=1
        # return count

        # better solution 
        mapping = {"X":1, "Y":-1, "." : 0}
        m, n = len(grid), len(grid[0])
        result = [[mapping[val] for val in row] for row in grid]
        xgrid = [[1 if val == 'X' else 0 for val in row] for row in grid]
        prefix = [[0]*n for _ in range(m)]
        xprefix = [[0]*n for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                prefix[i][j]=result[i][j]
                xprefix[i][j] = xgrid[i][j]
                if i > 0:
                    prefix[i][j] += prefix[i-1][j]
                    xprefix[i][j] += xprefix[i-1][j]
                if j > 0 :
                    prefix[i][j] += prefix[i][j-1]
                    xprefix[i][j] += xprefix[i][j-1]
                if i> 0 and j>0 :
                    prefix[i][j] -= prefix[i-1][j-1]
                    xprefix[i][j] += xprefix[i-1][j-1]

                if prefix[i][j] == 0 and xprefix[i][j] >= 1:
                    count+=1
        return count