class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        
        rows = len(grid)
        cols = len(grid[0])
        rhombus_sums = set()

        for i in range(rows):
            for j in range(cols):
                rhombus_sums.add(grid[i][j]) # k=0
                k = 1
                while True:

                    if i-k < 0 or i+k >= rows or j-k < 0 or j+k >= cols:
                        break

                    total = 0

                    # edge 1: top -> right
                    x, y = i-k, j
                    for step in range(k):
                        total += grid[x+step][y+step]

                    # edge 2: right -> bottom
                    x, y = i, j+k
                    for step in range(k):
                        total += grid[x+step][y-step]

                    # edge 3: bottom -> left
                    x, y = i+k, j
                    for step in range(k):
                        total += grid[x-step][y-step]

                    # edge 4: left -> top
                    x, y = i, j-k
                    for step in range(k):
                        total += grid[x-step][y+step]

                    rhombus_sums.add(total)

                    k += 1

        result = sorted(rhombus_sums, reverse=True)

        return result[:3]       