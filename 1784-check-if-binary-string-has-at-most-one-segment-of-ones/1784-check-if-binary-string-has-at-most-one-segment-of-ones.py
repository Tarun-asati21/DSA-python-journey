class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if len(s) <= 2 :
            return True
        arr = [0]
        for i in range (1, len(s)):
            
            if s[i] == "1" :
                arr.append(i)
                distance = i - arr[len(arr)-2]
                if distance == 1 :
                    continue
                else :
                    return False
        return True
                