class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        m, n = len(grid), len(grid[0])

        i, j = 0, 0
        visited = {(0, 0)}

        while True:
            direction = grid[i][j]

            if direction == 'L':
                ni, nj = i, j - 1
            elif direction == 'R':
                ni, nj = i, j + 1
            elif direction == 'U':
                ni, nj = i - 1, j
            else:
                ni, nj = i + 1, j

            if not (0 <= ni < m and 0 <= nj < n):
                break

            if (ni, nj) in visited:
                break

            i, j = ni, nj
            visited.add((i, j))

        return [i, j]