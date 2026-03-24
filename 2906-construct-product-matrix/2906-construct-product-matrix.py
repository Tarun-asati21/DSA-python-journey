class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # brute froce solution : TC =O(n^4)
        # better solution : TC=O(n^2) --> internally break due to int large size --> overflow situation
        # m, n = len(grid),len(grid[0])
        # product_matrix = [[0]*n for _ in range (m)]
        # product=1
        # for i in range(m):
        #     for j in range(n):
        #         product *= grid[i][j] 
        # product = product %12345
        # for i in range (m):
        #     for j in range(n):
        #         product_matrix[i][j] = int(product / grid[i][j])%12345
        # return product_matrix

        arr=[]
        for row in grid :
            for val in row :
                arr.append(val)
        size = len(arr)
        prefix = [1]*size
        suffix =[1]*size

        for i in range(1,size):
            prefix[i] = (prefix[i-1]*arr[i-1]) % 12345
        for i in range(size-2, -1,-1):
            suffix[i]=(suffix[i+1]*arr[i+1])%12345

        m, n = len(grid), len(grid[0])
        product = [[0]*n for _ in range(m)]
        idx=0
        for i in range(m):
            for j in range(n):
                product[i][j] = (prefix[idx]*suffix[idx])%12345
                idx+=1
        return product