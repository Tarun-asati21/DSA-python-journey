class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        temp=[]
        for i in range(len(mat)):
            count = sum(mat[i])
            temp.append((count, i))
        
        temp = sorted(temp)
        return [idx for _,idx in temp[:k]]
        