class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows , cols = len(grid),len(grid[0])

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        perimeter = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 :
                    degree = 0
                    for dr, dc in directions:
                        nr, nc = i + dr, j + dc
                        if (nr in range(rows) 
                            and nc in range(cols) 
                            and grid[nr][nc] == 1 ) :
                            degree += 1
                    perimeter += 4 - degree
        return perimeter