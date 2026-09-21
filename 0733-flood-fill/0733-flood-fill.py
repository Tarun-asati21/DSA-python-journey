class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:

        R, C = len(image), len(image[0])
        o_color = image[sr][sc]
        if o_color == color:
            return image
        def dfs(r, c):
            if image[r][c] == o_color:
                image[r][c] = color
                if r >= 1:
                    dfs(r-1, c)
                if r + 1 < R:
                    dfs(r + 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if c + 1 < C:
                    dfs(r, c + 1)

        dfs(sr, sc)
        return image

