class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        lst=[]
        for i in range(1, len(height)):
            if height[i-1]>threshold :
                lst.append(i)
        return lst
