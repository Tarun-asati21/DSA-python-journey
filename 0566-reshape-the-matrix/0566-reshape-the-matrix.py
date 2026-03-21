class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        column = len(mat[0])

        if row*column != r*c :
            return mat
        
        arr= []
        for i in range (0,row ):
            for j in range (0,column) :
                arr.append(mat[i][j])

        reshape = []
        i=0
        count=0
        while True :
            if count == row*column :
                break
            reshape.append(arr[i:i+c])
            i = i+c
            count += c
        return reshape

