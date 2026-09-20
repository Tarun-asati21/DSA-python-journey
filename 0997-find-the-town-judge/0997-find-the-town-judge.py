class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        # concept use : Degree of directed graph
        # edge case
        if n==1 :
            return 1

        freq = {}
        for edge in trust :
            # only assume degree is edge is pointing towards the town judge/person
            freq[edge[1]] = freq.get(edge[1], 0) + 1
        
        judge = -1
        for k,v in freq.items():
            if v == n-1 : # since exactly one given in question
                judge = k
                break
        
        for edge in trust :
            if edge[0] == judge :
                return -1
        return judge