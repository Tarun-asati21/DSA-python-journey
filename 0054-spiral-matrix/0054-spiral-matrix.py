class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        arr= []
        m = len(matrix)
        n  = len(matrix[0])   
        count = 0 
        round = 0
        while count < m*n :
            
            # top
            i=round
            for j in range(round, n-round):
                if count == m*n :
                    break
                arr.append(matrix[i][j])
                count+=1
            
            # right
            i = n-1-round
            for j in range(round+1, m-round):
                if count == m*n :
                    break
                arr.append(matrix[j][i])
                count+=1

            # bottom
            i = m-1-round
            for j in range(n-2-round , round-1, -1):
                if count == m*n :
                    break
                arr.append(matrix[i][j])
                count+=1
            
            # left
            i = round
            for j in range(m-2-round , round, -1 ):
                if count == m*n :
                    break
                arr.append(matrix[j][i])
                count += 1
            
            round += 1

        return arr


             