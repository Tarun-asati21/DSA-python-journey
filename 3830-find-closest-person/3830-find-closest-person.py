class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x_z = abs(x-z)
        y_z=abs(y-z)
        if x_z > y_z :
            return 2
        elif  x_z < y_z :
            return 1
        else :
            return 0