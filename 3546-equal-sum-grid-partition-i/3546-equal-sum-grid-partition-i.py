class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # brute force 
        row_arr = []
        total_sum = 0
        for row in grid :
            for val in row :
                row_arr.append(val)
                total_sum += val
        
        column_arr = []
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                column_arr.append(grid[j][i])
        
        sumi_1 = 0
        for i in range (len(grid[0]), len(row_arr), len(grid[0])):
            sumi_1 += sum(row_arr[i-len(grid[0]):i])
            sumi_2 = total_sum - sumi_1
            if sumi_1 == sumi_2 :
                return True 
        
        sumi_1 = 0
        for j in range(len(grid), len(column_arr), len(grid)):
            sumi_1 += sum(column_arr[j-len(grid):j])
            sumi_2 = total_sum - sumi_1
            if sumi_1 ==sumi_2 :
                return True
        
        return False