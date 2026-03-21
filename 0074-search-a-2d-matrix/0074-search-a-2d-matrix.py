class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if matrix[0][0] > target or matrix[-1][-1] < target :
            return False 
        
        
        for i in range(0, len(matrix)):
            if matrix[i][0] <= target and matrix[i][-1] >=  target :
                l = 0
                r = len(matrix[i])-1
                while l <= r :
                    mid = (l+r)//2
                    if matrix[i][mid] == target :
                        return True
                    elif matrix[i][mid] < target :
                        l = mid+1
                    else :
                        r = mid-1
        return False


        