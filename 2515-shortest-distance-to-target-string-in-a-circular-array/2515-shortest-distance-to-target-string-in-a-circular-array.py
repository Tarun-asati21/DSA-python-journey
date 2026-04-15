class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        origin = startIndex
        idx =  startIndex 
        steps = 0 
        while True :
            temp = words[idx]
            if  temp == target :
                front_step = steps
                break
            idx = (idx+1)%n 
            steps += 1
            if idx == origin :
                front_step = float("inf")
                break
        
        xdi = startIndex 
        steps = 0
        while True :
            temp = words[xdi]
            if temp == target :
                back_step  = steps
                break
            xdi = (xdi-1+n)%n 
            steps += 1
            if xdi == origin :
                back_step = float("inf")
                break
        
        if min(front_step, back_step) == float("inf") :
            return -1 
        else :
            return min(front_step, back_step)