class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        grid = [row[:] for row in mat]  # They are different objects
        m,n = len(mat), len(mat[0])
        for a in range(k) :
            for i in range (m) :
                if i%2 == 0 :
                    for j in range (n-1) :
                        mat[i][j], mat[i][j+1] = mat[i][j+1], mat[i][j] 
                else :
                    for j in range(n-1, 0, -1 ):
                        mat[i][j], mat[i][j-1] = mat[i][j-1], mat[i][j]

        return mat==grid


        
            