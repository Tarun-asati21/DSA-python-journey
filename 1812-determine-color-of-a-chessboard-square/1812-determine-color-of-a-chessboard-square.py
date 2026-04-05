class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if coordinates[0] in ["a","c","e","g"] :
            if int(coordinates[1]) % 2 == 0 :
                return True 
            return False
        else :
            if int(coordinates[1]) % 2 == 0 :
                return False
            return True
