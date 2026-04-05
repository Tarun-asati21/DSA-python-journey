class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x,y = 0,0
        idx  = 0
        while idx < len(moves) :
            if moves[idx] == "R" :
                x += 1
            elif moves[idx] == "L" :
                x-=1
            elif moves[idx] == "U" :
                y+=1
            else :
                y-=1
            idx += 1
        return x==0 and y==0
        
        # tc =O(n)  and SC=O(1)