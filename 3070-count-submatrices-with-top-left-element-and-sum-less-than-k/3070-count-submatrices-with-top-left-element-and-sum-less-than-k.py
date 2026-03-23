class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        # brute force solution : sum from idx [0,0] to [i,j rectangles
        # TLE : since TC = O(n^4)
        # m, n = len(grid), len(grid[0])
        # count =0
        # for i in range(m):
        #     for j in range(n):
        #         sumi=0
        #         for x in range(i+1) :
        #             for y in range(j+1):
        #                 sumi+=grid[x][y]
        #         if sumi <= k :
        #             count+=1
        # return count

        # better solution --> prefix sum use 
        m,n = len(grid), len(grid[0])
        prefix_sum_matrix = [[0]*n for _ in range(m)]
        count=0
        for i in range(m):
            for j in range(n):
                prefix_sum_matrix[i][j]=grid[i][j]

                if i > 0 : # add top
                    prefix_sum_matrix[i][j] += prefix_sum_matrix[i-1][j]
                if j > 0 : # add left
                    prefix_sum_matrix[i][j] += prefix_sum_matrix[i][j-1]
                if i>0 and j>0 : # subtract overlap
                    prefix_sum_matrix[i][j] -= prefix_sum_matrix[i-1][j-1]
                
                if prefix_sum_matrix[i][j] <= k :
                    count+=1
        return count 