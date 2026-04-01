class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        temp_x = bin(x)[2:].zfill(32)
        temp_y =  bin(y)[2:].zfill(32)
        count=0
        for i in range(len(temp_x)):
            if temp_x[i] != temp_y[i] :
                count +=1
        return count