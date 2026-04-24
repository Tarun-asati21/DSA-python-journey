class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        def occur(s, ch) :
            count = 0 
            for letter in s :
                if letter == ch :
                    count += 1
            return count 

        temp1 = moves.replace("_", "L")
        temp2 = moves.replace("_","R")

        L_move_1 = occur(temp1, "L")
        R_move_1 = occur(temp1, "R")
        dist_1 = abs(L_move_1 - R_move_1)

        L_move_2 = occur(temp2, "L")
        R_move_2 = occur(temp2, "R")
        dist_2 = abs(L_move_2 - R_move_2)

        return max(dist_1, dist_2)

        