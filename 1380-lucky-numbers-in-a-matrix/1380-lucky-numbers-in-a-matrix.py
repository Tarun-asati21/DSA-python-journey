class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        r = len(matrix)
        c = len(matrix[0])
        count = []

        for i in range (r) :
            for j in range(c) :
                if matrix[i][j] == min(matrix[i]) :
                    a=[]
                    for k in range(r) :
                        a.append(matrix[k][j])
                    if matrix[i][j] == max(a) :
                        count.append(matrix[i][j])
        return count
